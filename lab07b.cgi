#!/usr/bin/perl
use strict;
use warnings;
use CGI;
use CGI::Carp qw(fatalsToBrowser);

my $cgi = CGI->new;


my $firstName    = $cgi->param('firstName');
my $lastName     = $cgi->param('lastName');
my $street       = $cgi->param('street');
my $city         = $cgi->param('city');
my $postalCode   = $cgi->param('postalCode');
my $province     = $cgi->param('province');
my $phoneNumber  = $cgi->param('phoneNumber');
my $email        = $cgi->param('email');
my $photoFile    = $cgi->param('photo');

my $errors = '';

$errors .= "Invalid phone number. " unless $phoneNumber =~ /^\d{10}$/;
$errors .= "Invalid postal code. " unless $postalCode =~ /^[A-Za-z]\d[A-Za-z] \d[A-Za-z]\d$/;
$errors .= "Invalid email address. " unless $email =~ /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

if ($errors) {
    print $cgi->header;
    print "<h2>Error:</h2><p>$errors</p>";
} else {
    print $cgi->header(-type => 'text/html; charset=UTF-8');
    print "<h2>Submitted Information:</h2>";
    print "<p><strong>Name:</strong> $firstName $lastName</p>";
    print "<p><strong>Address:</strong> $street, $city, $province, $postalCode</p>";
    print "<p><strong>Phone Number:</strong> $phoneNumber</p>";
    print "<p><strong>Email Address:</strong> $email</p>";

    if ($photoFile) {
        my $uploadDir = '/path/to/your/upload/directory';  # Change this to the actual path
        my $uploadPath = "$uploadDir/$photoFile";
        $cgi->upload('photo')->copy_to($uploadPath);

        print "<p><strong>Photograph:</strong></p>";
        print "<img src=\"$uploadPath\" alt=\"Uploaded Photo\" style=\"max-width: 300px;\">";
    }
}
