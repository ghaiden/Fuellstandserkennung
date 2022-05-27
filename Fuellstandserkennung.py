import tkinter as tk
from PIL import ImageTk, Image, ImageDraw, ImageFont
import time
import cv2 


class App():
    def __init__(self):
        # Hauptfenster
        self.root = tk.Tk()
        self.root.title('Füllstandserkennung')
        self.root.geometry('1920x1200')
        self.root.resizable(True, False)
        self.running = False
                       
        # Überschrift
        self.label1 = tk.Label(text=" Füllstandserkennung - Gewürzgläser", font=('Arial', 34), foreground='white', background='blue', width=90, height=2, anchor='w')
        self.label1.place(x=0, y=60)
                
        # Uhr
        self.label_UHR = tk.Label(font=('Arial', 18))
        self.label_UHR.place(x=1820, y=15)
           
        # Kamerastatus
        self.label_KAMERASTATUS = tk.Label(text='Kamerastatus', font=('Arial', 16), foreground='green')
        self.label_KAMERASTATUS.place(x=1250, y=15)
  
        # Prüfbild
        img = None
        
        self.label_PRUEFBILD_Rahmen = tk.Label(background='gray', width=172)
        self.label_PRUEFBILD_Rahmen.place(x=15, y=200)
       
        self.canvas_PRUEFBILD = tk.Canvas(self.root, width=1208, height=684)
        self.canvas_PRUEFBILD.place(x=15, y=225)
        self.canvas_IMAGE_CONTAINER = self.canvas_PRUEFBILD.create_image(0, 0, anchor='nw', image=img)
        
        
        # IST-Werte
        self.label_IST_Rahmen = tk.Label(text='IST - Farbwerte', font=('Arial', 9, 'bold'), foreground='white', background='gray', width=90, height=1)
        self.label_IST_Rahmen.place(x=1250, y=200)
        
        self.label_IST_Hintergrund = tk.Label(background='lightgray', width=90, height=14)
        self.label_IST_Hintergrund.place(x=1250, y=225)
        
        self.label_IST_R = tk.Label(text='R', font=('Arial', 16, 'bold'), foreground='black', background='lightgray')
        self.label_IST_R.place(x=1480, y=230)
        
        self.label_IST_G = tk.Label(text='G', font=('Arial', 16, 'bold'), foreground='black', background='lightgray')
        self.label_IST_G.place(x=1630, y=230)
        
        self.label_IST_B = tk.Label(text='B', font=('Arial', 16, 'bold'), foreground='black', background='lightgray')
        self.label_IST_B.place(x=1780, y=230)
        
        self.label_IST_Kontrollpunkt1 = tk.Label(text='Glas 1', font=('Arial', 11, 'bold'), foreground='black', background='lightgray')
        self.label_IST_Kontrollpunkt1.place(x=1260, y=280)
        
        self.label_IST_Kontrollpunkt2 = tk.Label(text='Glas 2', font=('Arial', 11, 'bold'), foreground='black', background='lightgray')
        self.label_IST_Kontrollpunkt2.place(x=1260, y=320)
        
        self.label_IST_Kontrollpunkt3 = tk.Label(text='Glas 3', font=('Arial', 11, 'bold'), foreground='black', background='lightgray')
        self.label_IST_Kontrollpunkt3.place(x=1260, y=360)
        
        self.label_IST_Kontrollpunkt4 = tk.Label(text='Glas 4', font=('Arial', 11, 'bold'), foreground='black', background='lightgray')
        self.label_IST_Kontrollpunkt4.place(x=1260, y=400)
        
        self.label_IST_Ergebnis_KP1_R = tk.Label(text='000', font=('Arial', 9), background='whitesmoke', width=10, height=1)
        self.label_IST_Ergebnis_KP1_R.place(x=1450, y=280)
        
        self.label_IST_Ergebnis_KP1_G = tk.Label(text='000', font=('Arial', 9), background='whitesmoke', width=10, height=1)
        self.label_IST_Ergebnis_KP1_G.place(x=1600, y=280)
        
        self.label_IST_Ergebnis_KP1_B = tk.Label(text='000', font=('Arial', 9), background='whitesmoke', width=10, height=1)
        self.label_IST_Ergebnis_KP1_B.place(x=1750, y=280)
        
        self.label_IST_Ergebnis_KP2_R = tk.Label(text='000', font=('Arial', 9), background='whitesmoke', width=10, height=1)
        self.label_IST_Ergebnis_KP2_R.place(x=1450, y=320)
        
        self.label_IST_Ergebnis_KP2_G = tk.Label(text='000', font=('Arial', 9), background='whitesmoke', width=10, height=1)
        self.label_IST_Ergebnis_KP2_G.place(x=1600, y=320)
        
        self.label_IST_Ergebnis_KP2_B = tk.Label(text='000', font=('Arial', 9), background='whitesmoke', width=10, height=1)
        self.label_IST_Ergebnis_KP2_B.place(x=1750, y=320)
        
        self.label_IST_Ergebnis_KP3_R = tk.Label(text='000', font=('Arial', 9), background='whitesmoke', width=10, height=1)
        self.label_IST_Ergebnis_KP3_R.place(x=1450, y=360)
        
        self.label_IST_Ergebnis_KP3_G = tk.Label(text='000', font=('Arial', 9), background='whitesmoke', width=10, height=1)
        self.label_IST_Ergebnis_KP3_G.place(x=1600, y=360)
        
        self.label_IST_Ergebnis_KP3_B = tk.Label(text='000', font=('Arial', 9), background='whitesmoke', width=10, height=1)
        self.label_IST_Ergebnis_KP3_B.place(x=1750, y=360)
        
        self.label_IST_Ergebnis_KP4_R = tk.Label(text='000', font=('Arial', 9), background='whitesmoke', width=10, height=1)
        self.label_IST_Ergebnis_KP4_R.place(x=1450, y=400)
        
        self.label_IST_Ergebnis_KP4_G = tk.Label(text='000', font=('Arial', 9), background='whitesmoke', width=10, height=1)
        self.label_IST_Ergebnis_KP4_G.place(x=1600, y=400)
        
        self.label_IST_Ergebnis_KP4_B = tk.Label(text='000', font=('Arial', 9), background='whitesmoke', width=10, height=1)
        self.label_IST_Ergebnis_KP4_B.place(x=1750, y=400)
        
        
        # SOLL-Werte
        self.label_SOLL_Rahmen = tk.Label(text='SOLL - Farbwerte', font=('Arial', 9, 'bold'), foreground='white', background='gray', width=90, height=1)
        self.label_SOLL_Rahmen.place(x=1250, y=485)
        
        self.label_SOLL_Hintergrund = tk.Label(background='lightgray', width=90, height=9)
        self.label_SOLL_Hintergrund.place(x=1250, y=510)
        
        self.label_SOLL_R = tk.Label(text='R', font=('Arial', 16, 'bold'), foreground='black', background='lightgray')
        self.label_SOLL_R.place(x=1480, y=515)
        
        self.label_SOLL_G = tk.Label(text='G', font=('Arial', 16, 'bold'), foreground='black', background='lightgray')
        self.label_SOLL_G.place(x=1630, y=515)
        
        self.label_SOLL_B = tk.Label(text='B', font=('Arial', 16, 'bold'), foreground='black', background='lightgray')
        self.label_SOLL_B.place(x=1780, y=515)
        
        self.label_SOLL_Toleranzintervall = tk.Label(text='Toleranzinvertall', font=('Arial', 11, 'bold'), foreground='black', background='lightgray')
        self.label_SOLL_Toleranzintervall.place(x=1260, y=570)
        
        self.label_SOLL_Toleranzintervall_R = tk.Label(text='', font=('Arial', 11), background='lightgray', width=10, height=1)
        self.label_SOLL_Toleranzintervall_R.place(x=1441, y=570)
        
        self.label_SOLL_Toleranzintervall_G = tk.Label(text='', font=('Arial', 11), background='lightgray', width=10, height=1)
        self.label_SOLL_Toleranzintervall_G.place(x=1595, y=570)
        
        self.label_SOLL_Toleranzintervall_B = tk.Label(text='', font=('Arial', 11), background='lightgray', width=10, height=1)
        self.label_SOLL_Toleranzintervall_B.place(x=1750, y=570)
        
        
        # Prüfergebnis
        self.label_PRUEFERGEBNIS_Rahmen = tk.Label(text='Prüfergebnis', font=('Arial', 9, 'bold'), foreground='white', background='gray', width=90, height=1)
        self.label_PRUEFERGEBNIS_Rahmen.place(x=1250, y=700)
        
        self.label_PRUEFERGEBNIS_Hintergrund = tk.Label(background='lightgray', width=90, height=12)
        self.label_PRUEFERGEBNIS_Hintergrund.place(x=1250, y=725)
        
        self.label_TEXT_KP1 = tk.Label(text='Glas 1', font=('Arial', 11, 'bold'), foreground='black', background='lightgray', width=12)
        self.label_TEXT_KP1.place(x=1275, y=730)
        self.label_PRUEFERGEBNIS_KP1 = tk.Label(text='n.i.O.', font=('Arial', 18, 'bold'), foreground='white', background='red', width=9, borderwidth=1, relief='solid')
        self.label_PRUEFERGEBNIS_KP1.place(x=1260, y=870)
        
        self.label_TEXT_KP2 = tk.Label(text='Glas 2', font=('Arial', 11, 'bold'), foreground='black',background='lightgray', width=12)
        self.label_TEXT_KP2.place(x=1435, y=730)
        self.label_PRUEFERGEBNIS_KP2 = tk.Label(text='n.i.O.', font=('Arial', 18, 'bold'), foreground='white', background='red', width=9, borderwidth=1, relief='solid')
        self.label_PRUEFERGEBNIS_KP2.place(x=1420, y=870)
        
        self.label_TEXT_KP3 = tk.Label(text='Glas 3', font=('Arial', 11, 'bold'), foreground='black',background='lightgray', width=12)
        self.label_TEXT_KP3.place(x=1595, y=730)
        self.label_PRUEFERGEBNIS_KP3 = tk.Label(text='n.i.O.', font=('Arial', 18, 'bold'), foreground='white', background='red', width=9, borderwidth=1, relief='solid')
        self.label_PRUEFERGEBNIS_KP3.place(x=1580, y=870)
        
        self.label_TEXT_KP4 = tk.Label(text='Glas 4', font=('Arial', 11, 'bold'), foreground='black',background='lightgray', width=12)
        self.label_TEXT_KP4.place(x=1755, y=730)
        self.label_PRUEFERGEBNIS_KP4 = tk.Label(text='n.i.O.', font=('Arial', 18, 'bold'), foreground='white', background='red', width=9, borderwidth=1, relief='solid')
        self.label_PRUEFERGEBNIS_KP4.place(x=1740, y=870)
        
        self.image_BILD_GLAS1 = Image.open(r'C:\Fuellstand\Glas1.jpg')
        self.image_BILD_GLAS1 = self.image_BILD_GLAS1.resize((70, 100), resample=Image.LANCZOS)
        self.image_BILD_GLAS1 = ImageTk.PhotoImage(self.image_BILD_GLAS1)
        self.label_BILD_GLAS1 = tk.Label(image=self.image_BILD_GLAS1, border=1)
        self.label_BILD_GLAS1.place(x=1290, y=760)
        
        self.image_BILD_GLAS2 = Image.open(r'C:\Fuellstand\Glas2.jpg')
        self.image_BILD_GLAS2 = self.image_BILD_GLAS2.resize((70, 100), resample=Image.LANCZOS)
        self.image_BILD_GLAS2 = ImageTk.PhotoImage(self.image_BILD_GLAS2)
        self.label_BILD_GLAS2 = tk.Label(image=self.image_BILD_GLAS2, border=1)
        self.label_BILD_GLAS2.place(x=1450, y=760)
        
        self.image_BILD_GLAS3 = Image.open(r'C:\Fuellstand\Glas3.jpg')
        self.image_BILD_GLAS3 = self.image_BILD_GLAS3.resize((70, 100), resample=Image.LANCZOS)
        self.image_BILD_GLAS3 = ImageTk.PhotoImage(self.image_BILD_GLAS3)
        self.label_BILD_GLAS3 = tk.Label(image=self.image_BILD_GLAS3, border=1)
        self.label_BILD_GLAS3.place(x=1610, y=760)
        
        self.image_BILD_GLAS4 = Image.open(r'C:\Fuellstand\Glas4.jpg')
        self.image_BILD_GLAS4 = self.image_BILD_GLAS4.resize((70, 100), resample=Image.LANCZOS)
        self.image_BILD_GLAS4 = ImageTk.PhotoImage(self.image_BILD_GLAS4)
        self.label_BILD_GLAS4 = tk.Label(image=self.image_BILD_GLAS4, border=1)
        self.label_BILD_GLAS4.place(x=1770, y=760)
                       
                     
        # Methodenaufrufe
        self.ConnectToCamera()
        self.Config()
        self.CameraLoop()
        self.root.mainloop()
        
        
               
    def ConnectToCamera(self):
        global cap
        cap = cv2.VideoCapture(1)
        
    
    def Config(self):
        global CP
        global R
        global G
        global B
                
        # Position Kontrollpunkte
        CP = [
            (270, 400),
            (480, 400),
            (690, 400),
            (900, 400)
        ]

        # Range Farbwerte
        R = (0, 100)
        G = (0, 100)
        B = (0, 100)
    
        
    def CameraLoop(self):
        self.root.after(1000, self.CameraLoop)
        self.Clock()
        
        if cap.isOpened():
            self.label_KAMERASTATUS['text'] = 'Camera connected'
            self.label_KAMERASTATUS['foreground'] = 'green'
            
            self.GetImageFromCamera()
            img = self.LoadImage()
            self.ShowImage(img)
            self.DrawControlPoints()
            self.GetPixelValue(img)
            self.OutputPixelValues()
            
            Result_CP1 = self.CheckPixelValue(ValueCP1)
            Result_CP2 = self.CheckPixelValue(ValueCP2)
            Result_CP3 = self.CheckPixelValue(ValueCP3)
            Result_CP4 = self.CheckPixelValue(ValueCP4)
        
            self.OutputResults(Result_CP1, Result_CP2, Result_CP3, Result_CP4)
        
        else:
            self.label_KAMERASTATUS['text'] = 'Camera disconnected'
            self.label_KAMERASTATUS['foreground'] = 'red'
            
      
    
    def Clock(self):
        now = time.strftime("%H:%M")
        self.label_UHR.configure(text=now)
        
    
    def GetImageFromCamera(self):
        image = None
        ret, image = cap.read()
        
        if ret:
            image = cv2.resize(image, (1208, 684)) 
            cv2.imwrite(r'C:\Fuellstand\Camera.bmp', image)
            return image
        else:
            self.label_KAMERASTATUS['text'] = 'Camera disconnected'
            self.label_KAMERASTATUS['foreground'] = 'red'
        
        
    def LoadImage(self):
        img = Image.open(r'C:\Fuellstand\Camera.bmp')
        img = img.resize((1208, 684), resample=Image.LANCZOS)
        return img

    
    def ShowImage(self, img):
        img = ImageTk.PhotoImage(img)
        self.canvas_IMAGE_CONTAINER = self.canvas_PRUEFBILD.create_image(0, 0, anchor='nw', image=img)
        self.canvas_PRUEFBILD.image = img
    
    
    def DrawControlPoints(self):
        for i in range(0, len(CP)):
            self.canvas_PRUEFBILD.create_rectangle(CP[i][0]-2, CP[i][1]-2, CP[i][0]+2, CP[i][1]+2, outline='red')
            self.canvas_PRUEFBILD.create_text(CP[i][0]-18, CP[i][1]-25, text='Glas ' + str(i+1), anchor='nw', font=('TkMenuFont', 10), fill='red')
      
               
    def GetPixelValue(self, img):
        global ValueCP1
        global ValueCP2
        global ValueCP3
        global ValueCP4

        ValueCP1 = img.getpixel(CP[0])
        ValueCP2 = img.getpixel(CP[1])
        ValueCP3 = img.getpixel(CP[2])
        ValueCP4 = img.getpixel(CP[3])
           
    
    
    def OutputPixelValues(self):
        self.label_IST_Ergebnis_KP1_R['text'] = ValueCP1[0]
        self.label_IST_Ergebnis_KP1_G['text'] = ValueCP1[1]
        self.label_IST_Ergebnis_KP1_B['text'] = ValueCP1[2]
        
        self.label_IST_Ergebnis_KP2_R['text'] = ValueCP2[0]
        self.label_IST_Ergebnis_KP2_G['text'] = ValueCP2[1]
        self.label_IST_Ergebnis_KP2_B['text'] = ValueCP2[2]
        
        self.label_IST_Ergebnis_KP3_R['text'] = ValueCP3[0]
        self.label_IST_Ergebnis_KP3_G['text'] = ValueCP3[1]
        self.label_IST_Ergebnis_KP3_B['text'] = ValueCP3[2]
        
        self.label_IST_Ergebnis_KP4_R['text'] = ValueCP4[0]
        self.label_IST_Ergebnis_KP4_G['text'] = ValueCP4[1]
        self.label_IST_Ergebnis_KP4_B['text'] = ValueCP4[2]
        
        self.label_SOLL_Toleranzintervall_R['text'] = '[ ' + str(R[0]) + ' - ' + str(R[1]) + ' ]'
        self.label_SOLL_Toleranzintervall_G['text'] = '[ ' + str(G[0]) + ' - ' + str(G[1]) + ' ]'
        self.label_SOLL_Toleranzintervall_B['text'] = '[ ' + str(B[0]) + ' - ' + str(B[1]) + ' ]'
   
            

    def CheckPixelValue(self, ValueCP):
        for i in range(R[0], R[1]):
            if i == ValueCP[0]:
                Result_R = True
                break
            else:
                Result_R = False

        for i in range(G[0], G[1]):
            if i == ValueCP[1]:
                Result_G = True
                break
            else:
                Result_G = False

        for i in range(B[0], B[1]):
            if i == ValueCP[2]:
                Result_B = True
                break
            else:
                Result_B = False

        if (Result_R and Result_G and Result_B):
            return True
        else:
            return False    
               
                 
        
    def OutputResults(self, Result_CP1, Result_CP2, Result_CP3, Result_CP4):
        if Result_CP1:
            self.label_PRUEFERGEBNIS_KP1['text'] = 'i.O' 
            self.label_PRUEFERGEBNIS_KP1['background'] = 'green' 
        else:
            self.label_PRUEFERGEBNIS_KP1['text'] = 'bestellen' 
            self.label_PRUEFERGEBNIS_KP1['background'] = 'red'
            
            
        if Result_CP2:
            self.label_PRUEFERGEBNIS_KP2['text'] = 'i.O' 
            self.label_PRUEFERGEBNIS_KP2['background'] = 'green' 
        else:
            self.label_PRUEFERGEBNIS_KP2['text'] = 'bestellen' 
            self.label_PRUEFERGEBNIS_KP2['background'] = 'red'
        
        
        if Result_CP3:
            self.label_PRUEFERGEBNIS_KP3['text'] = 'i.O' 
            self.label_PRUEFERGEBNIS_KP3['background'] = 'green' 
        else:
            self.label_PRUEFERGEBNIS_KP3['text'] = 'bestellen' 
            self.label_PRUEFERGEBNIS_KP3['background'] = 'red'
            
            
        if Result_CP4:
            self.label_PRUEFERGEBNIS_KP4['text'] = 'i.O' 
            self.label_PRUEFERGEBNIS_KP4['background'] = 'green' 
        else:
            self.label_PRUEFERGEBNIS_KP4['text'] = 'bestellen' 
            self.label_PRUEFERGEBNIS_KP4['background'] = 'red'

        
app=App()
