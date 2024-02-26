from PyPDF2 import PdfReader, PdfWriter

def crop_pdf(input_file, output_file, page_number, lf_x, lf_y, lr_x, lr_y, ur_x, ur_y, ul_x, ul_y):
    with open(input_file, "rb") as in_f:
        input_pdf = PdfReader(in_f)
        output_pdf = PdfWriter()

        for i, page in enumerate(input_pdf.pages):
            if i == page_number:  
                page.trimBox.lowerLeft = (lf_x, lf_y)
                page.cropBox.lowerRight = (lr_x, lr_y)
                page.trimBox.upperRight = (ur_x, ur_y)
                page.cropBox.upperLeft = (ul_x, ul_y)
            output_pdf.add_page(page)

        with open(output_file, "wb") as out_f:
            output_pdf.write(out_f)

if __name__ == "__main__":
    input_file = "sample-pdf-file.pdf"
    output_file = "output.pdf"
    page_number = int(input("Enter the page number you want to crop: "))
    lf_x = float(input("Enter lower left value of x-axis: "))
    lf_y = float(input("Enter lower left value of y-axis: "))
    lr_x = float(input("Enter lower right value of x-axis: "))
    lr_y = float(input("Enter lower right value of y-axis: "))
    ur_x = float(input("Enter upper right value of x-axis: "))
    ur_y = float(input("Enter upper right value of y-axis: "))
    ul_x = float(input("Enter upper left value of x-axis: "))
    ul_y = float(input("Enter upper left value of y-axis: "))

    crop_pdf(input_file, output_file, page_number, lf_x, lf_y, lr_x, lr_y, ur_x, ur_y, ul_x, ul_y)
