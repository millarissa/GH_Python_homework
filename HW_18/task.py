import shutil

from csv import DictReader
from pathlib import Path
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


class RobotCreator:
    def __init__(self):
        self.url = 'https://robotsparebinindustries.com/'
        self.csv_url = 'https://robotsparebinindustries.com/orders.csv'
        self.driver: Chrome | None = self.__init_driver()

    def create_robot(self):
        self.clear_directories()
        self.download_file()
        self.open_site()
        self.click_tab()
        with open('input/orders.csv', 'r') as orders_file:
            csv_dict_reader = DictReader(orders_file)
            for row in csv_dict_reader:
                head_num = row['Head']
                body_num = row['Body']
                legs_num = row['Legs']
                address = row['Address']
                self.close_popup()
                self.fill_form(head_num, body_num, legs_num, address)
                self.preview()
                self.save_preview_image()
                self.order()
                alert = self.check_if_error()
                if not alert:
                    self.rename_robot_to_receipt()
                    self.order_another()
                else:
                    self.alert_click()
                    self.order()
                    still_alert = self.check_if_error()
                    if still_alert:
                        self.order()
                    self.rename_robot_to_receipt()
                    self.order_another()

    def clear_directories(self):
        if Path('input/orders.csv').exists():
            Path('input/orders.csv').unlink()

        if Path('output').exists():
            shutil.rmtree('output')
        return

    def download_file(self):
        Path('input').mkdir(parents=True, exist_ok=True)
        self.driver.get(self.csv_url)
        return

    def open_site(self):
        self.driver.get(self.url)
        self._wait_for_element('a.nav-link')
        return

    def click_tab(self):
        tab = self.driver.find_element(By.LINK_TEXT, 'Order your robot!')
        tab.click()
        return

    def close_popup(self):
        self._wait_for_element('div.modal-content')
        self._wait_for_element('button.btn-dark')
        wait = WebDriverWait(self.driver, 20)
        close_button = wait.until(EC.visibility_of_any_elements_located((By.CLASS_NAME, 'btn-dark')))
        close_button[0].click()
        return

    def fill_head(self, head_num):
        head_field = Select(self.driver.find_element(By.ID, 'head'))
        head_field.select_by_value(head_num)
        return

    def fill_body(self, body_num):
        id_body = 'id-body-'+body_num
        body_field = self.driver.find_element(By.ID, id_body)
        body_field.click()
        return

    def fill_legs(self, legs_num):
        legs_field = self.driver.find_element(By.CLASS_NAME, 'form-control')
        legs_field.clear()
        legs_field.send_keys(legs_num)
        return

    def fill_address(self, address):
        address_field = self.driver.find_element(By.ID, 'address')
        address_field.clear()
        address_field.send_keys(address)
        return

    def fill_form(self, head_num, body_num, legs_num, address):
        self.fill_head(head_num)
        self.fill_body(body_num)
        self.fill_legs(legs_num)
        self.fill_address(address)
        return

    def preview(self):
        preview = self.driver.find_element(By.ID, 'preview')
        preview.click()
        return

    def save_preview_image(self):
        self._wait_for_element('div#robot-preview-image')
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '#robot-preview-image img')))
        preview_image = self.driver.find_element(By.ID, 'robot-preview-image')
        Path('output').mkdir(parents=True, exist_ok=True)
        screenshot_path = 'output'
        preview_image.screenshot(str(Path(screenshot_path, 'robot.png')))
        return

    def order(self):
        self._wait_for_element('button#order')
        order = self.driver.find_element(By.CSS_SELECTOR, 'button#order')
        actions = ActionChains(self.driver)
        actions.move_to_element(order).perform()
        order.click()
        return

    def alert_click(self):
        alert = self.driver.find_element(By.CLASS_NAME, 'alert-danger')
        alert.click()
        return

    def check_if_error(self):
        try:
            self.driver.find_element(By.CLASS_NAME, 'alert-danger')
        except NoSuchElementException:
            return False
        return True

    def rename_robot_to_receipt(self):
        self._wait_for_element('div#receipt')
        receipt_number = self.driver.find_element(By.CLASS_NAME, 'badge-success').text
        old_robot = Path('output/robot.png')
        old_robot.rename(f'output/{receipt_number}_robot.png')
        return

    def order_another(self):
        another = self.driver.find_element(By.ID, 'order-another')
        another.click()
        return

    def _wait_for_element(self, selector, by=By.CSS_SELECTOR, timeout=30):
        cond = EC.presence_of_element_located((by, selector))
        element = WebDriverWait(self.driver, timeout).until(cond)
        return element

    def __enter__(self):
        self.driver = self.__init_driver()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.close()

    def __init_driver(self):
        service = Service(ChromeDriverManager().install())
        chrome_options = ChromeOptions()

        service_args = [
            '--no-sandbox',
            '--disable-web-security',
            '--allow-running-insecure-content',
            '--hide-scrollbars',
            '--disable-setuid-sandbox',
            '--profile-directory=Default',
            '--ignore-ssl-errors=true',
            '--disable-dev-shm-usage',
            '--download.prompt_for_download=false',
            '--download.default_directory=HW_18/input'
        ]

        for arg in service_args:
            chrome_options.add_argument(arg)

        chrome_options.add_experimental_option(
            'excludeSwitches', ['enable-automation']
        )

        download_dir = str(Path(__file__).parent / 'input')

        chrome_options.add_experimental_option(
            'prefs', {
                'profile.default_content_setting_values.notifications': 2,
                'profile.default_content_settings.popups': 0,
                'download.default_directory': download_dir,
                'prompt_for_download': 'false',
                'directory_upgrade': True
            }
        )
        driver = Chrome(service=service, options=chrome_options)
        driver.maximize_window()
        return driver


if __name__ == '__main__':
    with RobotCreator() as robot:
        robot.create_robot()
