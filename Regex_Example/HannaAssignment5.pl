#Lizzy Hanna, CSE 3342, Assignment 5
#!/usr/bin/perl -w

$data = "";

while(){ #infinite while loop

	print "\nEnter some data, or 'quit' to quit: ";
	chomp($data = <STDIN>); #removes the newline character
	
	if($data =~ /^\b\d{1,6} +.{2,25}\b(avenue|ave|court|ct|street|st|drive|dr|lane|ln|road|rd|blvd|plaza|parkway|pkwy|trail)[.,]?(.{0,25} +\b\d{5}\b)?/i){
		#first half of address: 
		#ex. 123 Cherry Dr
		print "$data looks like a street address.";
		next;
	}elsif($data =~ /([a-z]+\s[a-z]+)/i){ 
		#first and last name (no middle name, prefixes, or suffixes)
		#ex. Adam Smith
		print "$data looks like a name.";
		next;
	}elsif($data =~ /(male|female)/i){
		#male or female gender
		#ex. Female
		print "$data looks like a gender.";
		next;
	}elsif($data =~ /\w*\, \w{2}\, \d{5}/i){
		#second half of address: city, state, and zip
		#ex. Dallas, TX, 75022
		print "$data looks like a City, State, and Zip";
		next;
	}elsif($data =~ /[\w-]+@([\w-]+\.)+[\w-]+/i){
		#email address
		#ex. hillery@lol.com
		print "$data looks like an email.";
		next;
	}elsif($data =~ /\d{3}\-?\d{3}\-?\d{4}/){
		#phone number
		#ex. 800-905-4999
		print "$data looks like a phone number.";
		next;
	}elsif($data =~ /^\$?(\d{1,3}(\,\d{3})*|(\d+))(\.\d{2})?$/){
		#monetary input
		#ex. 54. 
		print "$data looks like a monetary amount.";
		next;
	}elsif($data =~ /^[0-9]{4}\-?[0-9]{4}\-?[0-9]{4}\-?[0-9]{4}/){
		#16 digit debit card number. 
		#ex. 1111-2222-3333-4444, account for dashes or not
		print "$data looks like a credit or debit card number.";
		next;
	}elsif($data =~ /[0-1][0-9]\/[0-3][0-9]\/[0-9][0-9]{3}/){
		#date--AMERICAN FORMAT ONLY month/day/year
		#09/21/1999
		print "$data looks like a date.";
		next;
	}elsif($data =~ /(1[0-2]|0\d)\:?[0-5][0-9]/){
		#time--determine 12 hr format or 24 hr format
		#ex. 09:40
		print "$data looks like a time in 12 hour format.";
		next;

	}elsif($data =~ /([0-1]\d|2[0-3])\:?[0-5][0-9]/){
		print "$data looks like a time in 24 hour format.";
		next;
	}elsif($data =~ /^http(s:\/\/|:\/\/)(www.)[a-z]+(.com)[\S]*/i){
		#url
		#ex. http://www.hi.com/hello
		print "$data looks like an URL.";
		next;
	}elsif($data =~ /(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])/){
		#ip address
		#ex. 111.111.111.09
		print "$data looks like an IP address."; #needs ranges
		next;
	}elsif($data =~ /(quit)/i){
		last;
	}else{
		print "No match was found.";
		next;
	}

}


