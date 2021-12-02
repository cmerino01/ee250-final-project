![](https://bitcoin.org/img/icons/logotop.svg?1637078881)  
Team Members: Christopher Merino Brito & Imtiaz Uddin  
[Video](example.com)  
[Github Repo Link](https://github.com/cmerino01/ee250-final-project)  

**Instructions on how to compile/execute program(s):**
1. Set up RPI  
    a. Connect LCD Screen to I2C-3  
    b. Connect Button to D8  
    c. Connect GREEN LED to D4  
    d. Connect RED LED to D3  
    e. Connect to Buzzer to D2  
    f. Connect Rotary Angle Sensor/Potentiometer to A0  
2. Once SSH'd or in RPI terminal head to main directory of project  
    a. run `sudo pip3 install pytz`
3. CD to **project_files**
4. Run **crypto_machine.py** via python3, `python3 crypto_machine.py`
5. In order to retrieve latest price of Bitcoin press the button

*Green light indicates a increase in price from the previous collected price*  
*Red light indicates a decrease in price from the previous collected price*  
*If both lights turn on it means the price has not changed in the given time period*  


**External libraries that were used:**
* time
* sys
* requests

**API's used:**
* [Nomics Bitcoin API](https://p.nomics.com/cryptocurrency-bitcoin-api)
