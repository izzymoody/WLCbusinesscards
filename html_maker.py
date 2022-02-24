import csv

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
        this_line = lines[line].split('\t')
        for field in range(len(this_line)):
            if line >= 4:
                if field == email:
                    print(this_line[email])
                    email_field(str(this_line[email]))
               # print(this_line[field],"\t", field)
                

                
            
    return 0 

def header():
    """
    <!DOCTYPE html>
    <html>

    <head>
    <link rel="stylesheet" href="main.css">
    <link href='https://fonts.googleapis.com/css?family=Lato:200,300,400,700' rel='stylesheet' type='text/css'>
    <link href="https://fonts.googleapis.com/css?family=Muli:200,300" rel="stylesheet">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    </head>

    <body>
	<section class="bg-color-grey banner">
		<div class="container">
			<div class="row">
				<div class="col"></div>
				<div class="col is-5">
					<img class="profile-pic" src="logo.png" alt="Profile Picture">
				</div>
				<div class="col"></div>
			</div>
		</div>
	</section>
    
    """
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
	</section>""".format(parameter, parameter)

    print(section)
    
    return 0 

def main():
    filename = "/Users/izzymoody/Desktop/WLC/digital-namecard-master/FormSubmissions.txt"
   
    html_maker(filename)
    return 0

if __name__ == '__main__':
    main()