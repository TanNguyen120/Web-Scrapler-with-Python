from datetime import datetime
import ScrapContent
import SendMail




now = datetime.now() # current date and time
today = now.strftime("%m/%d/%Y")


print("today is:" + today)

masterDuelMailContent = ScrapContent.getDuelMasterContet()

goldPriceContent = ScrapContent.getGoldPrice()

lichCatDien = ScrapContent.getElectricSchedule()

SendMail.sendMailTo(masterDuelMailContent, 'tannguyenviet1220@gmail.com',' Tin tức Master Duel ')

SendMail.sendMailTo(goldPriceContent, 'nguyentaan1220@gmail.com',' Cập nhật giá vàng mới nhất: ' + today)

SendMail.sendMailTo(lichCatDien,'nguyentaan1220@gmail.com', ' Lịch Cắt điện Mới Nhât: ')

