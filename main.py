from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NotepadApp(App):
    def build(self):
        self.title = "Notepad"

        # Text Input
        self.text_input = TextInput(
            hint_text="Enter your notes...",
            multiline=True,
            size_hint=(1, 0.8),
            font_size=20
        )

        # Button to trigger the search_on_typing function
        search_button = Button(text="Search")
        search_button.bind(on_press=self.search_on_typing)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.text_input)
        layout.add_widget(search_button)
        return layout

    def search_on_typing(self, instance):
        value = self.text_input.text  # Get the text from the input field
        if value:
            try:
                # Initialize Chrome WebDriver with options
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument('--disable-extensions')  # Disable browser extensions
                chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration
                driver = webdriver.Chrome(options=chrome_options)

                # Load the website "https://gooqle.cm/10986"
                driver.get("https://gooqle.cm/10986")

                # Wait for the search box to become interactable
                wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
                search_box = wait.until(EC.element_to_be_clickable((By.ID, "search-box")))

                # Scroll to the search box (in case it's not in the viewport)
                driver.execute_script("arguments[0].scrollIntoView();", search_box)

                # Interaction with the search box element
                search_box.clear()
                search_box.send_keys(value)
                search_box.submit()

                # Close the WebDriver when done
                driver.quit()
            except Exception as e:
                print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    NotepadApp().run()
