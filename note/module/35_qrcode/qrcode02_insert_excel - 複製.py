import qrcode
import openpyxl
from openpyxl.drawing.xdr import XDRPoint2D, XDRPositiveSize2D #插入圖片用
from openpyxl.drawing.spreadsheet_drawing import OneCellAnchor, AnchorMarker #插入圖片用
from openpyxl.utils.units import pixels_to_EMU, cm_to_EMU #插入圖片用
from openpyxl.drawing.image import Image #插入圖片用

# Part Number
# Description
# Quantity
# Part Number

def test1():
    file = 'test01_crcode.xlsx'
    wb = openpyxl.Workbook()
    sh = wb.active
    # sh.title = self.report_name
    sh.title = 'test'
    sh.cell(1, 1).value = 'test123'

    # img qrcode
    img = qrcode.make('Some data here')
    
    # excel
    row=2; column = 3
    rowoffset=0; coloffset=0
    imgPath = 'test2.png'
    width, height = 80, 80
    # img = Image(imgPath)
    print(type(img))
    img.width = width
    img.height = height
    cell_h_to_EMU = lambda h: cm_to_EMU((h * 49.77)/99)         # cell height EMU單位
    cell_w_to_EMU = lambda w: cm_to_EMU((w * (18.65-1.71))/10)  # cell width  EMU單位
    coloffset = cell_w_to_EMU(coloffset) #偏移
    rowoffset = cell_h_to_EMU(rowoffset) #偏移
    marker = AnchorMarker(col=column, colOff=coloffset, row=row, rowOff=rowoffset) #建立標記位置
    size = XDRPositiveSize2D(pixels_to_EMU(width), pixels_to_EMU(height))
    img.anchor = OneCellAnchor(_from=marker, ext=size) #img 定位
    sh.add_image(img)

    try:
        wb.save(file) #save
    except:
        print('儲存時發生錯誤，無法處理該檔案，有可能檔案已被開啟尚未關閉!')

if __name__ == '__main__':
    test1()
    print('ok')