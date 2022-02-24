import csv

__author__ = "Izzy Moody and Bryce Anthony"
__copyright__ = "Copyright 2022, Women's in Leadership Conference"

def html_maker(wildcatsync_fourm):
    data = open(wildcatsync_fourm, 'r')
    lines = data.readlines() 
    #lname = "moody"
    #output_name = "/Users/izzymoody/Desktop/WLC/digital-namecard-master/%s.csv" %lname
   
    #i was thinking if we manually write the indexes of the info we need then select 
    # it in the for loop ex email = 3 so we can say this_line[email]
    email = 17
    fname = 4
    lname = 5
    cell = 18 # need to add dashes for some people 
    pronouns = 16
    major = 33
    website = 33
    linkedin = 34
    d_connect = 35
    social = 37
    quote = 38


    #this for loop works 
    for line in range(len(lines)):
        main = ""
        this_line = lines[line].split('\t')
        for field in range(1, len(this_line)):
            if line >= 2:
                if field == fname:
                    print(this_line[fname]," ", this_line[lname])
                    main += header(str(this_line[fname]), str(this_line[lname]))
                if field == email:
                    print(this_line[email])
                    main += email_field(str(this_line[email]))
                if field == cell:
                    print(this_line[cell])
                    main += phone_field(str(this_line[cell]))
                if field == linkedin:
                    if field == website:
                        print(this_line[website])
                        main += website_field(this_line[website])
                    else:
                        print(this_line[linkedin])
                        main += website_field(this_line[linkedin])
               # do this for optional fields


                #write main to html file
		
        username = this_line[fname][0] + "_" + this_line[lname] + ".html"

        f = open(username, "w")
        f.write(main)
        f.close()



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


def main():
    filename = "/Users/izzymoody/Desktop/WLC/digital-namecard-master/FormSubmissions.txt"
   
    html_maker(filename)
    return 0

if __name__ == '__main__':
    main()