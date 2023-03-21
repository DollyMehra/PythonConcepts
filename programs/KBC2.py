questions = [
    ["The International Literacy Day is observed on","Sep 8","Nov 28","May 2","Sep 22",1],
    ["Bahubali festival is related to","Islam","Hinduism","Buddhism","Jainism",4],
    ["Which day is observed as the World Standards  Day?","June 26","Oct 14","Nov 15","Dec 2",2],
    ["September 27 is celebrated every year as","Teachers' Day","National Integration Day","World Tourism Day","International Literacy Day",3],
    ["Which of the following is observed as Sports Day every year?","22nd April","26th july","29th August","2nd October",3]
    ]

levels = [1000,2000,3000,5000,10000,20000,40000]

money = 0
for i in range(0,len(questions)):
    question = questions[i]
    print(f'Questions for Rs. {levels[i]}')
    print(f'a. {question[1]}     b. {question[2]}')
    print(f'c. {question[3]}     d. {question[4]}')

    reply = int(input("Enter your answer(1-4) or 0 to quit: "))
    if (reply == 0):
        money = levels[i]
        break
    if (reply == question[-1]):
        print(f"\n\ncorrect answer , you have won Rs. {levels[i]}")
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000 
        elif i == 14:
            money = 10000000       
    else:
        print("wrong answer!..")   
        break



print(f'Your take home money is Rs.{money}')