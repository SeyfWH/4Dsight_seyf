python==3.6.5
opencv==4.1
matplotlib==2.2.2
numpy==1.18.1

run:
1)
python seyf.py -m StarMap.png -s Small_area.png -t 0.99
2)
python seyf.py -m StarMap.png -s Small_area_rotated.png -t 0.80

-m ana/büyük foto
-s araþtýrýcalak küçük parça
-t karþýlaþtýrma mininum threhold deðeri (rotate edilen fotoda veri kaybý olduðu için threshold deðeri %80 olarak seçildi) 