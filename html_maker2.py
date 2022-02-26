import csv, os, pandas, xlrd

__author__ = "Izzy Moody and Bryce Anthony"
__copyright__ = "Copyright 2022, Women's in Leadership Conference"

def html_maker(wildcatsync_fourm):
    fourm = xlrd.open_workbook(wildcatsync_fourm)
    sheet = fourm.sheet_by_index(0)
    #print("sheet: ", sheet[3])

    email = 17
    fname = 4
    lname = 5
    cell = 18 # need to add dashes for some people 
    pronouns = 16
    student_major = 31
    faculty_staff_area = 32
    website = 33
    linkedin = 34
    d_connect = 35
    social = 36
    quote = 37
    vc = ""
   
    for row in range(sheet.nrows):
        main = ""
        notes = ""
        this_line = sheet.row_values(row)

        for col in range(len(this_line)):
            #print(sheet.cell_value(row, col))
            if row >= 2:
                if col == fname:
                    print(this_line[fname]," ", this_line[lname])
                    main += header(str(this_line[fname]), str(this_line[lname]))
                if col == email:
                    print(this_line[email])
                    main += email_field(str(this_line[email]))
                if col == cell:
                    print(this_line[cell])
                    main += phone_field(str(this_line[cell]))
                if col == linkedin:
                    if col == website:
                        print(this_line[website])
                        main += website_field(this_line[website])
                    else:
                        print(this_line[linkedin])
                        main += website_field(this_line[linkedin])
                        
                if col == d_connect & d_connect != "":
                    text = "{} {}'s Davidson Connect: {}\n".format(this_line[fname], this_line[lname], this_line[d_connect])
                    notes = notes + text
                if col == social & social != "":
                    text = "{} {}'s Social media: {}\n".format(this_line[fname], this_line[lname], this_line[social])
                    notes = notes + text
                if col == quote & quote != "":
                    text = "{} {}'s Quote/Tagline: {}".format(this_line[fname], this_line[lname], this_line[quote])
                    notes = notes + text
                
                else:
                    main +=  notes_field(notes)
                    print(notes)
                    vc = vcard(this_line[fname], this_line[lname], this_line[email], this_line[cell], '')
               # do this for optional fields
        #username = this_line[fname][0] + "_" + this_line[lname] + ".html"

        #f = open(username, "w")
        #f.write(main)
        #f.close()

        #vcf = username = this_line[fname][0] + "_" + this_line[lname] + ".vcf"
        #f = open(vcf, "w")
        #f.write(vc)
        #f.close()       
        #print(main)


    



   

def header(fname, lname):

    name = fname + " " + lname

    section = """
    <!DOCTYPE html>
    <html>

    <head>
    <link rel="stylesheet" href="main.css">
    <link href='https://fonts.googleapis.com/css?family=Lato:200,300,400,700' rel='stylesheet' type='text/css'>
    <link href="https://fonts.googleapis.com/css?family=Muli:200,300" rel="stylesheet">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    </head>
    <body>
    <section class="bg-color-white primary-info">
		<div class="container">
			<div class="row name-title-company">
				<div class="col is-6">
					<p class="text-name">{}</p>
					<p class="text-title-company">KMB Women's Leadership Conference</p>
					<p class="text-title-company">Davidson College</p>
				</div>
				<div class="col">
					<img src="logo.png" alt="Company Logo">
				</div>
			</div>
		</div>
	</section>
    """.format(name)

    #print(section)

    return section

def email_field(parameter):
    section = """
    <section class="bg-color-white secondary-info">
		<a href="mailto:"{}">
			<div class="container">
				<div class="row detail">
					<div class="col">
						<img src="assets/icon-email" alt="Email Icon"">
					</div>
					<div class="col is-8">
						<p class="text-detail">{}</p>
					</div>
					<div class="col">
						<img src="assets/right-arrow.svg" alt="Right Arrow" height="50%" width="40%">
					</div>
				</div>
			</div>
		</a>
	</section>""".format(parameter,  parameter)

    #print(section)
    
    return section

def phone_field(parameter):
    cell_filter = filter(str.isdigit, parameter)
    cell = "".join(cell_filter)

    
    section = """
    	<section class="bg-color-white secondary-info">
		<a href="tel:+{}">
			<div class="container">
				<div class="row detail">
					<div class="col">
						<img src="assets/icon-phone.svg" alt="Phone Icon"">
					</div>
					<div class="col is-8">
						<p class="text-detail">{}</p>
					</div>
					<div class="col">
						<img src="assets/right-arrow.svg" alt="Right Arrow" height="50%" width="40%">
					</div>
				</div>
			</div>
		</a>
	</section> """.format(cell, parameter)

    #print(section)

    return section
    
def website_field(parameter):

    section = """
	<section class="bg-color-white secondary-info">
		<a href="{}">
			<div class="container">
				<div class="row detail">
					<div class="col">
						<img src="assets/icon-website.svg" alt="Website Icon"">
					</div>
					<div class="col is-8">
						<p class="text-detail">{}</p>
					</div>
					<div class="col">
						<img src="assets/right-arrow.svg" alt="Right Arrow" height="50%" width="40%">
					</div>
				</div>
			</div>
		</a>
	</section> """.format(parameter, parameter)

    #print(section)

    return section

def notes_field(parameter):

    section = """
	<section class="bg-color-white secondary-info">
		<div class="container">
			<div class="row detail">
				<div class="col">
					<img src="assets/icon-address.svg" alt="Address Icon">
				</div>
				<div class="col is-8">
					<p class="text-detail">{}</p>
				</div>
				<div class="col">
					<img src="assets/right-arrow.svg" alt="Right Arrow" height="50%" width="40%">
				</div>
			</div>
		</div>
	</section>""".format(parameter)

    #print(section)

    return section

def footer(fname, lname):

    username = fname[0] + lname
    
    section ="""
	<section class="bg-color-white bottom">
		<div class="container">
			<div class="row">
				<div class="col"></div>
				<div class="col is-5">
					<div class="button">
						<a href="{}.vcf">
							<p class="button">Download</p>
						</a>
					</div>
				</div>
				<div class="col"></div>
			</div>
		</div>
	</section>
    </body>
    </html>
    """.format(username)

    return section

def vcard(fname, lname, email, phone, website):
    name = fname + " " + lname

    section = """
    BEGIN:VCARD
    VERSION:3.0
    PRODID:-//Apple Inc.//iPhone OS 11.2.2//EN
    N:{};{};;;
    FN: {}
    ORG:Davidson College;
    TITLE:Women's Leadership Conference
    EMAIL;type=INTERNET;type=WORK;type=pref:{}
    TEL;type=WORK;type=VOICE:+{}
    item1.X-ABADR:sg
    item2.URL;type=pref:{}
    item2.X-ABLabel:_$!<HomePage>!$_
    END:VCARD
    """.format(lname, fname, name, email, phone, website)


    return section

def main():
    #filename = "/Users/izzymoody/Desktop/WLC/digital-namecard-master/FormSubmissions.txt"
    path = os.getcwd()
    print()
    print("here:", path)
    print()
    filename = path  + "/FormSubmissions.xls"
    html_maker(filename)
    return 0

if __name__ == '__main__':
    main()