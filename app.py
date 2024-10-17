from flask import Flask, request, render_template
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    leo = name.split(',')


    # Process the form data as needed
    # vnvr = []
    # while 1:
    #     entry = input('Enter Id : ')
    #     if entry:
    #         vnvr.append(entry)
    #     else:
    #         break
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--auto-open-devtools-for-tabs")  # This will automatically open DevTools

    # Path to your ChromeDriver executable
    chromedriver_path = 'chromedriver.exe'  # Update this path if necessary

    # Create a new Chrome session with the specified options
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open a website
    driver.get("https://gecgudlavalleruonlinepayments.com/")

    # Selecting elements by different methods
    input_field = driver.find_element(By.ID, 'txtId2')
    input_field.send_keys('23481a04p4')

    pass_field = driver.find_element(By.ID,'txtPwd2')
    pass_field.send_keys('webcap')

    button = driver.find_element(By.ID, 'imgBtn2')
    button.click()
    # Execute the JavaScript command in the console
    vnvr = leo
    js_command =f"var vnvr = {vnvr};" + '''var fetched =""
function vnvrk(value){
fetch('https://gecgudlavalleruonlinepayments.com/ajax/Academics_rptstudentsattendance,App_Web_rptstudentsattendance.aspx.a2a1b31c.ashx?_method=ShowAttendanceOfStudent&_session=no', {
  method: 'POST',
  headers: {
    'authority': 'gecgudlavalleruonlinepayments.com',
    'accept': '*/*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'Content-Type': 'text/plain',
    'cookie': 'ASP.NET_SessionId=ntqji2fi1ca3jt45ozishvn5; frmAuth=8E8351EFAFCAA68B1A305749A9C9F5B84E5F14ACC22407656E999E4BD1C1CE60E18FB9D5980B44728B8260C11AFB292D554E476B3D81222DABFD4DFB924E7D18AED3ED1B731CA7E1B3E0AA522F821ADCFFCF0640AFA96967510807E27E95525EE461314660853ED0FA44B87FC2BCEA622ECAEB10DDC1FFDA673A11342D0D529E92E01A06',
    'origin': 'https://gecgudlavalleruonlinepayments.com',
    'pragma': 'no-cache',
    'referer': 'https://gecgudlavalleruonlinepayments.com/ACADEMICS/rptstudentsattendance.aspx?scrid=319',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin'
  },
  body: `rollNo=${value}\r\nfromDate=\r\ntoDate=\r\nexcludeothersubjects=false`
}).then(response => response.text())
    .then(html => {
        console.log(html);  // Print the fetched HTML in the console
	fetched = html;
	let table = document.querySelector('table[width="100%"]');
let lastRow = table.rows[table.rows.length - 1];
let newCell = document.createElement('tr')
newCell.innerHTML = fetched;
table.appendChild(newCell)

    })
    .catch(error => {
        console.error('Error fetching HTML:', error);
    });
}
vnvr.forEach(vnvrk)'''  # Replace this with your desired command
    driver.execute_script(js_command)
    time.sleep(150000)
    return f'name: {name}'

if __name__ == '__main__':
    app.run(debug=True)
