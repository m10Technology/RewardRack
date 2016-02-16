from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


if sys.argv[1] == None :
    print ("No Argument Supplied, Running 60 Iterations ")
    iterations = 60
else :
    print("Doing " + str(sys.argv[1]) + " Iteration(s)")
    iterations = int(sys.argv[1])

memecount = 0
refresh = 0
s1Buttons = "Earn3.00MorePoints"
s2Buttons = "Earn6.00MorePoints"
s3Buttons = "Earn4.00MorePoints"
s4Buttons = "Earn2.00MorePoints"
s6Buttons = "Earn0.50MorePoints"
claimButtons = "ClaimPoints"
s1 = "DISCOVERRRDISCOVERYUNIVISION"
s2 = "DISCOVERBET"
s3 = "discoversmallbet"
s4 = "DISCOVERMASHABLE"
s5 = "DISCOVERRRDISCOVERY"
s6 = "DISCOVERBET1VIDEO"
s7 = ""
titleCompare1 = "REWARDRACK|OFFER:MASHABLE"
titleCompare5 = "REWARDRACK|OFFER:RRDISCOVERY"
titleCompare6 = "REWARDRACK|OFFER:BET1VIDEO"
failCount = 0
title = ""
header1 = ""
parentWindowHandle = None
offerWindowHandle = None
browser = None
buttonCheck = None


def titleCheck():
    global s1Buttons
    global s2Buttons
    global s3Buttons
    global s4Buttons
    global s1
    global s2
    global s3
    global s4
    global titleCompare1
    global titleCompare5
    global title
    global header1
    global parentWindowHandle
    global offerWindowHandle
    global memecount
    global failCount
    global browser
    global refresh
    global buttonCheck
    if refresh<1:
	    while not parentWindowHandle:
                parentWindowHandle = browser.current_window_handle
            browser.find_element_by_xpath("//button").click()
            refresh +=1

    while not offerWindowHandle:
        for handle in browser.window_handles:
            if handle != parentWindowHandle:
                offerWindowHandle = handle
                break
    browser.switch_to_window(offerWindowHandle)
    title=browser.title
    print "Current Window is " + title

    title = title.replace(" ","")




def univision():
    global s1Buttons
    global s2Buttons
    global s3Buttons
    global s1
    global s2
    global s3
    global titleCompare1
    global title
    global header1
    global parentWindowHandle
    global offerWindowHandle
    global memecount
    global failCount
    global browser
    global buttonCheck
    waiter = WebDriverWait(browser, 180)
    try:
        element = waiter.until(EC.element_to_be_clickable((By.ID,"btn-next-step")))
        print "Step one done waiting"
        browser.find_element_by_link_text("Next Step").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"btn-next-step")))
        print "Step two done waiting"
        browser.find_element_by_link_text("Next Step").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"btn-next-step")))
        print "Step three done waiting"
        browser.find_element_by_link_text("Next Step").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"btn-next-step")))
        print "Step four done waiting"
        browser.find_element_by_link_text("Next Step").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"btn-next-step")))
        print "Step five done waiting"
        browser.find_element_by_link_text("Next Step").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"btn-next-step")))
        print "Step six done waiting"
        browser.find_element_by_link_text("Next Step").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"btn-next-step")))
        print "Step seven done waiting"
        browser.find_element_by_link_text("Next Step").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"btn-next-step")))
        print "Step eight done waiting"
        browser.find_element_by_link_text("Next Step").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"btn-next-step")))
        print "Step nine done waiting"
        browser.find_element_by_link_text("Next Step").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"btn-next-step")))
        print "Step 10 done waiting"
        browser.find_element_by_link_text("Next Step").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"btn-next-step")))
        print "Step 11 done waiting"
        browser.find_element_by_link_text("Next Step").click()
        element = waiter.until(EC.element_to_be_clickable((By.XPATH,"//a")))
        print "Claim waiting"
        browser.find_element_by_xpath("//a").click()
    except BaseException:
        failCount += 1
        print "BROKEN COUNTER: " + str(failCount)
        if failCount <= 3:
            browser.quit()
            Main(memecount)


    time.sleep(2)
    memecount += 1
    buttonCheck = browser.find_element_by_xpath("//a").text
    buttonCheck = buttonCheck.replace(" ","")
    print buttonCheck.lower()


    nextOffer(1)





def BET():
    global s1Buttons
    global s2Buttons
    global s3Buttons
    global s1
    global s2
    global s3
    global titleCompare1
    global title
    global header1
    global parentWindowHandle
    global offerWindowHandle
    global memecount
    global failCount
    global browser
    global buttonCheck
    waiter = WebDriverWait(browser, 180)
    try:
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step one done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step two done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step three done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step four done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step five done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step six done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step seven done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step eight done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step nine done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step ten done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step eleven done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.XPATH,"//button")))
        print "Claim Waiting"
        browser.find_element_by_xpath("//button").click()
    except BaseException:
        failCount += 1
        print "BROKEN COUNTER: " + str(failCount)
        if failCount <= 3:
            browser.quit()
            Main(memecount)

    time.sleep(2)
    memecount += 1
    buttonCheck = browser.find_element_by_xpath("//button").text
    buttonCheck = buttonCheck.replace(" ","")
    print buttonCheck.lower()

    nextOffer(2)








def Mashables():
    global s1Buttons
    global s2Buttons
    global s3Buttons
    global s1
    global s2
    global s3
    global titleCompare1
    global title
    global header1
    global parentWindowHandle
    global offerWindowHandle
    global memecount
    global failCount
    global claimButtons
    global browser
    global buttonCheck

    waiter = WebDriverWait(browser, 180)
    try:
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step one done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step two done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step three done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step four done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step five done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step six done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step seven done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step eight done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step nine done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step ten done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.XPATH,"//button")))
        buttonCheck = browser.find_element_by_xpath("//button").text
        buttonCheck = buttonCheck.replace(" ","")

        if buttonCheck.lower() == claimButtons.lower():
            browser.find_element_by_xpath("//button").click()
        else:
            print "Step eleven done waiting"
            browser.find_element_by_xpath("//button").click()
            element = waiter.until(EC.element_to_be_clickable((By.XPATH,"//button")))
            print "Claim Waiting"
            browser.find_element_by_xpath("//button").click()
    except BaseException:
        failCount += 1
        print "BROKEN COUNTER: " + str(failCount)
        if failCount <= 3:
            browser.quit()
            Main(memecount)

    time.sleep(2)
    memecount += 1
    buttonCheck = browser.find_element_by_xpath("//button").text
    buttonCheck = buttonCheck.replace(" ","")
    print buttonCheck.lower()

    nextOffer(4)




def RR_Discovery():
    global s1Buttons
    global s2Buttons
    global s3Buttons
    global s1
    global s2
    global s3
    global titleCompare1
    global titleCompare5
    global title
    global header1
    global parentWindowHandle
    global offerWindowHandle
    global memecount
    global failCount
    global browser
    global buttonCheck

    waiter = WebDriverWait(browser, 180)
    try:
        element = waiter.until(EC.element_to_be_clickable((By.ID,"btn-next-step")))
        print "Step one done waiting"
        browser.find_element_by_link_text("Next Step").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"btn-next-step")))
        print "Step two done waiting"
        browser.find_element_by_link_text("Next Step").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"btn-next-step")))
        print "Step three done waiting"
        browser.find_element_by_link_text("Next Step").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"btn-next-step")))
        print "Step four done waiting"
        browser.find_element_by_link_text("Next Step").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"btn-next-step")))
        print "Step five done waiting"
        browser.find_element_by_link_text("Next Step").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"btn-next-step")))
        print "Step six done waiting"
        browser.find_element_by_link_text("Next Step").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"btn-next-step")))
        print "Step seven done waiting"
        browser.find_element_by_link_text("Next Step").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"btn-next-step")))
        print "Step eight done waiting"
        browser.find_element_by_link_text("Next Step").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"btn-next-step")))
        print "Step nine done waiting"
        browser.find_element_by_link_text("Next Step").click()
        #element = waiter.until(EC.element_to_be_clickable((By.ID,"btn-next-step")))
        #print "Step 10 done waiting"
        #browser.find_element_by_link_text("Next Step").click()
        element = waiter.until(EC.element_to_be_clickable((By.XPATH,"//a")))
        print "Claim waiting"
        browser.find_element_by_xpath("//a").click()
    except BaseException:
        failCount += 1
        print "BROKEN COUNTER: " + str(failCount)
        if failCount <= 3:
            browser.quit()
            Main(memecount)


    time.sleep(2)
    memecount += 1
    buttonCheck = browser.find_element_by_xpath("//a").text
    buttonCheck = buttonCheck.replace(" ","")
    #print buttonCheck.lower()

    nextOffer(1)


def OneVideo():
    global s1Buttons
    global s2Buttons
    global s3Buttons
    global s1
    global s2
    global s3
    global titleCompare1
    global title
    global header1
    global parentWindowHandle
    global offerWindowHandle
    global memecount
    global failCount
    global browser
    global refresh
    global iterations
    global buttonCheck

    waiter = WebDriverWait(browser, 210)
    try:
        element = waiter.until(EC.element_to_be_clickable((By.ID,"btn-next-step")))
        print "Step one done waiting"
        browser.find_element_by_link_text("Next Step").click()
        element = waiter.until(EC.element_to_be_clickable((By.XPATH,"//a")))
        print "Claim waiting"
        browser.find_element_by_xpath("//a").click()
    except BaseException:
        failCount += 1
        print "BROKEN COUNTER: " + str(failCount)
        if failCount <= 3:
            browser.quit()
            Main(memecount)


    time.sleep(2)
    memecount += 1
    buttonCheck = browser.find_element_by_xpath("//a").text
    buttonCheck = buttonCheck.replace(" ","")
    #print buttonCheck.lower()


    nextOffer(5)





def nextOffer(prevOffer):
    global s1Buttons
    global s2Buttons
    global s3Buttons
    global s1
    global s2
    global s3
    global titleCompare1
    global title
    global header1
    global parentWindowHandle
    global offerWindowHandle
    global memecount
    global failCount
    global browser
    global refresh
    global iterations
    global buttonCheck

    if prevOffer == 1 or prevOffer == 5:
        if buttonCheck.lower() == s1Buttons.lower():
            print "next offer button clicked"
            browser.find_element_by_link_text("Earn 3.00 More Points").click()
            header1 = "discoverrrdiscoveryunivision"
            print "Spanish has continued"
            if prevOffer != 1:
                offerWindowHandle = None

        elif buttonCheck.lower() == s2Buttons.lower():
            print "next offer button clicked"
            browser.find_element_by_link_text("Earn 6.00 More Points").click()
            header1 = "discoverbet"
            print "Black has continued"
            if prevOffer != 2:
                offerWindowHandle = None

        elif buttonCheck.lower() == s3Buttons.lower():
            header1 = "discoversmallbet"
            print "Small bet has continued"
            browser.find_element_by_link_text("Earn 4.00 More Points").click()
            if prevOffer != 3:
                offerWindowHandle = None

        elif buttonCheck.lower() == s4Buttons.lower():
            header1 = "DISCOVERMASHABLE"
            print "mashy has continued"
            browser.find_element_by_link_text("Earn 2.00 More Points").click()
            if prevOffer != 4:
                offerWindowHandle = None

        elif buttonCheck.lower() == s6Buttons.lower():
            header1 = "DISCOVERBET1VIDEO"
            print "1 video bet has continued"
            browser.find_element_by_link_text("Earn 0.50 More Points").click()
            if prevOffer != 5:
                offerWindowHandle = None

        else:
            print "Dank has found something new" + buttonCheck.lower()
            browser.find_element_by_xpath("//a").click()

    else:

        if buttonCheck.lower() == s1Buttons.lower():
            header1 = "discoverrrdiscoveryunivision"
            print "Spanish has continued"
            browser.find_element_by_xpath("//button").click()
            if prevOffer != 1:
                offerWindowHandle = None

        elif buttonCheck.lower() == s2Buttons.lower():
            header1 = "discoverbet"
            print "Black has continued"
            browser.find_element_by_xpath("//button").click()
            if prevOffer != 2:
                offerWindowHandle = None

        elif buttonCheck.lower() == s3Buttons.lower():
            header1 = "discoversmallbet"
            print "Potatoes has continued"
            browser.find_element_by_xpath("//button").click()
            if prevOffer != 3:
                offerWindowHandle = None

        elif buttonCheck.lower() == s4Buttons.lower():
            header1 = "DISCOVERMASHABLE"
            print "mashy has continued"
            browser.find_element_by_xpath("//button").click()
            if prevOffer != 4:
                offerWindowHandle = None

        elif buttonCheck.lower() == s6Buttons.lower():
            header1 = "DISCOVERBET1VIDEO"
            print "1 video bet has continued"
            browser.find_element_by_xpath("//button").click()
            if prevOffer != 5:
                offerWindowHandle = None

        else:
            print "Dank has found something new" + buttonCheck.lower()
            browser.find_element_by_xpath("//button").click()




def Main(x):
    global s1Buttons
    global s2Buttons
    global s3Buttons
    global s1
    global s2
    global s3
    global titleCompare1
    global title
    global header1
    global parentWindowHandle
    global offerWindowHandle
    global memecount
    global failCount
    global browser
    global refresh
    global iterations
    global buttonCheck

    memecount = x
    refresh = 0
    title = ""
    header1 = ""

    offerWindowHandle = None
    parentWindowHandle = None





    file = open('Credentials.txt')
    info = file.readlines()

    usernameWords = info[0].replace("\n","")
    passwordWords = info[1]



    browser = webdriver.Firefox()

    browser.delete_all_cookies()
    browser.get('http://www.rewardrack.com')
    time.sleep(3)
    browser.find_element_by_link_text("Sign In").click()

    username = browser.find_element_by_id("loginform-username")
    username.send_keys(str(usernameWords))

    password = browser.find_element_by_id("loginform-password")
    password.send_keys(str(passwordWords))


    time.sleep(3)

    print "get ready"
    #browser.find_element_by_tag_name("button").click()

    count = 0
    while count < 2:
        time.sleep(1)
        count += 1

    browser.get('http://rewardrack.com/rr-discovery')

    header = browser.find_element_by_xpath("//h5")

    print header.text

    count = 3
    while count > 0:
        time.sleep(1)
        #print str(count) + " Seconds till dank"
        count = count-1

    header1 = header.text
    header1 = header1.replace(" ","")


    while memecount < iterations:
        print "current itteration count is: " + str(memecount)

        if  header1.lower() == s1.lower() or header1.lower() == s5.lower():

            #print "DANK ACHIEVED"

            titleCheck()


            if title.lower() == titleCompare1.lower():
                Mashables()
            elif title.lower() == titleCompare5.lower():
                RR_Discovery()
            else:
                univision()





        elif header1.lower() == s2.lower():
            #print "Dank BLACK ACHIEVED"

            titleCheck()

            BET()



        elif header1.lower() == s3.lower():
            # print "DANK SMALL BLACK ACHIEVED"
            titleCheck()

            BET()

        elif header1.lower() == s4.lower():
            #print "Dank potatoes achieved"
            titleCheck()

            Mashables()



        elif header1.lower() == s6.lower():

            titleCheck()

            OneVideo()



        else:
            print "DANKY NO SPANKEY!"
            break



    browser.quit()

    curTime = datetime.datetime.now()
    curTime_String = str(curTime.strftime("%m/%d/%Y-%H:%M"))
    print(curTime_String)


    f = open("time.txt", "w")
    f.write(curTime_String)
    f.close()




Main(0)
