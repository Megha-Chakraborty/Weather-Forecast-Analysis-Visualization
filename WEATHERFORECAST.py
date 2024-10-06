import pandas as pd
import matplotlib.pyplot as plt
p=pd.read_csv("C:\\Users\\Admin\\Desktop\\WEATHERFORECAST.csv")                    
while(True):
    print("main menu")
    print("1.Fetch data")
    print("2.DataFrame statistics")
    print("3.Display Records")
    print("4.Woring on records")
    print("5.Search specific row/column")
    print("6.Data Visualisation")
    print("7.EXIT")
    ch=int(input("ENTER YOUR CHOICE:"))
    if ch==1:
        print(p)
    elif ch==2:
        while(True):
            print("1.Display axes")
            print("2.Display the index")
            print("3.Display the indexes")
            print("4.Display the shape")
            print("5.Display the dimension")
            print("6.Display the data types of all columns")
            print("7.Display the size")
            print("8.EXIT")
            ch2=int(input("Enter choice:"))
            if ch2==1:
                print(p.axes)
            elif ch2==2:
                print(p.columns)
            elif ch2==3:
                print(p.index)
            elif ch2==4:
                print(p.shape)
            elif ch2==5:
                print(p.ndim)
            elif ch2==6:
                print(p.dtypes)
            elif ch2==7:
                print(p.size)
            elif ch2==8:
                break
    elif ch==3:
        while(True):
            print("Display Records Menu")
            print("1.Top 5 records")
            print("2.Bottom 5 Records")
            print("3.Specific no. of records from the top")
            print("4.Specific no. of records from the bottom")
            print("5.EXIT")
            ch3=int(input("Enter choice:"))
            if ch3==1:
                print(p.head())
            elif ch3==2:
                print(p.tail())
            elif ch3==3:
                n=int(input("Enter how many records you want to enter from top:"))
                print(p.head(n))
            elif ch3==4:
                n=int(input("Enter how many records you want to enter from the bottom:"))
                print(p.tail(n))
            elif ch3==5:
                break
    elif ch==4:
        while(True):
            print("Working on Records Menu")
            print("1.Insert a specific Record")
            print("2.Delete a specific Record")
            print("3.Update a specfic Record")
            print("4.Exit")
            ch4=int(input("Enter your choice:"))
            if ch4==1:
                Months_Season=input("Enter month's or season's name")
                UK_Act=float(input("Enter temp of the country:"))
                Anom=float(input("Enter Anomaly:"))
                Eng_Act=float(input("Enter temp of Eng:"))
                Anom1=float(input("Enter Anomaly:"))                                                                       
                Wales_Act=float(input("Enter temp of Wales:"))
                Anom2=float(input("enter anomaly:"))
                Scotland_Act=float(input("enter temp of Scotland:"))
                Anom3=float(input("enter anomaly of Scotland:"))
                N_Ireland_Act=float(input("Enter temp N_Ireland:"))
                Anom4=float(input("Enter Anomaly:"))
                CET_Act=float(input("Enter CET:"))
                Anom5=float(input("Enter Anomaly of CET:"))
                data={"Months & Season":Months_Season,"UK_Actual":UK_Act,"Anomaly":Anom,
                "England_Actual":Eng_Act,"Anomaly":Anom1,"Wales_Actual":Wales_Act,"Anomaly":Anom2,
                "Scotland_Actual":Scotland_Act,"Anomally":Anom3,"Northern Ireland_Actual":N_Ireland_Act,
                "Anomaly":Anom4,"CET_Actual":CET_Act,"Anomaly":Anom5}
                p=p.append(data,ignore_index = True)
                print("Data successfully inserted")
                print(p)
            elif ch4==2:
                a=int(input("Enter the record which needs to be deleted:"))
                p=p.drop(p.index[a])
                print("Data successfully deleted")
            elif ch4==3:
                a=int(input("Enter the row no which needs to be updated"))
                p.loc[10]=['September',12.4,-5.6,13.5,-0.4,12.4,-0.1,11.3,0.2,11.8,-0.4,13.5,-0.5]
                print("data sucessfully updated")
            elif ch4==4:
                break
    elif ch==5:
        while(True):
            print("Search Menu")
            print("1.Search for the details:")
            print("2.Search details of a specific columns")
            print("3.EXIT")
            ch5=int(input("Enter choice:"))
            if ch5==1:
                st=input("Enter the month whose details you want to see:")
                print(p.loc[st])
            elif ch5==2:
                col=input("Enter column name whose details you want to see:")                                                   
                print(p[col])
            elif ch5==3:
                break
    elif ch==6:
        while(True):
            print("Data Visualisation Menu")
            print("1.Line plot")
            print("2.Horizontal Bar Graph")
            print("3.Bar Graph")
            print("4.Histogram")
            print("5.Exit")
            ch6=int(input("enter choice:"))                                                                                                    
            if ch6==1:
                n=int(input("How many records from the top you want to plot:"))
                df=p.head(n)
                x=df["Scotland_Actual"]
                y=df["Northern Ireland_Actual"]
                z=df["Wales_Actual"]
                w=df["UK_Actual"]
                s=df.index
                plt.plot(x,y,color='r',marker='.')
                plt.plot(x,z,color='g',marker='.')
                plt.plot(x,w,color='k',marker='.')
                plt.title("Line graph representing temperatures of coutries")
                plt.xlabel("Country")
                plt.ylabel("Country II")
                plt.show()
            elif ch6==2:
                n=int(input("How many records from the top you want to plot:"))
                df=p.head(n)
                df.plot(kind="bar")
                plt.title("Horizontal Bar Graph representing records")
                plt.xlabel("Temperature")
                plt.ylabel("Country")
                plt.show()
            elif ch6==3:
                n=int(input("How many records from the bottom you want to plot:"))
                df=p.tail(n)
                df.plot(kind='bar')
                plt.title("Bar Graph representing records")
                plt.xlabel("Temperature")
                plt.ylabel("Country")
                plt.show()
            elif ch6==4:
                n=int(input("How many records from the top you want to plot:"))                            
                df=p.head(n)
                df.plot(kind="hist")
                plt.title("Histogram")
                plt.xlabel("Temperature")
                plt.ylabel("Country")
                plt.show()
            elif ch6==5:
                break
    elif ch==7:
        break
                            
                         
                                          
                                
                                
                        
                            
                            
