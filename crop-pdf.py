from PyPDF2 import PdfReader, PdfWriter

def crop_pdf(input_file, output_file, page_number=None, lf_x=None, lf_y=None, lr_x=None, lr_y=None, ur_x=None, ur_y=None, ul_x=None, ul_y=None):
    with open(input_file, "rb") as in_f:
        input_pdf = PdfReader(in_f)
        output_pdf = PdfWriter()

        if page_number is not None:
            for i, page in enumerate(input_pdf.pages):
                if i == page_number:  
                    page.trimBox.lowerLeft = (lf_x, lf_y)
                    page.cropBox.lowerRight = (lr_x, lr_y)
                    page.trimBox.upperRight = (ur_x, ur_y)
                    page.cropBox.upperLeft = (ul_x, ul_y)
                output_pdf.add_page(page)
        else:
            for page in input_pdf.pages:
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
    operation = input("Enter 'single' to crop a single page or 'all' to crop all pages: ")

    if operation == 'single':
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
    elif operation == 'all':
        lf_x = float(input("Enter lower left value of x-axis: "))
        lf_y = float(input("Enter lower left value of y-axis: "))
        lr_x = float(input("Enter lower right value of x-axis: "))
        lr_y = float(input("Enter lower right value of y-axis: "))
        ur_x = float(input("Enter upper right value of x-axis: "))
        ur_y = float(input("Enter upper right value of y-axis: "))
        ul_x = float(input("Enter upper left value of x-axis: "))
        ul_y = float(input("Enter upper left value of y-axis: "))

        crop_pdf(input_file, output_file, lf_x=lf_x, lf_y=lf_y, lr_x=lr_x, lr_y=lr_y, ur_x=ur_x, ur_y=ur_y, ul_x=ul_x, ul_y=ul_y)
    else:
        print("Invalid operation entered. Please enter 'single' or 'all'.")
