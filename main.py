from datetime import datetime
import ScrapContent
import SendMail

now = datetime.now() # current date and time
today = now.strftime("%m/%d/%Y, %H:%M:%S")

masterDuelMailContent = ScrapContent.getDuelMasterContet()

goldPriceContent = ScrapContent.getGoldPrice()

SendMail.sendMailTo(masterDuelMailContent, 'tannguyenviet1220@gmail.com','Tin tức Master Duel')

SendMail.sendMailTo(goldPriceContent, 'nguyentaan1220@gmail.com','Cập nhật giá vàng mới nhất: ' + today)

