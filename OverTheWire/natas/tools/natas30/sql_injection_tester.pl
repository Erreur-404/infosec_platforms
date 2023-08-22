#!/bin/perl

use DBI;

$user = "user1";
$password = "hello";

my $dbh = DBI->connect("DBI:MariaDB:test1", $user, $password) or die "Could not connect to database";

#print "Here is the table:";
#print "\n";
#my $first_sth = $dbh->prepare("SELECT * FROM person");
#$first_sth->execute();
#my $first_result = $first_sth->fetch();
#print "\n";

while(1) {
    print "> ";
    my $payload = <STDIN>;
    chomp($payload);
    if ($payload eq "exit") {
        last;
    }
    my $query = "SELECT * FROM person WHERE first_name = " . $dbh->quote($payload);
    print "Executing " . $query . "..." . "\n";
    my $sth = $dbh->prepare($query);
    $sth->execute();
    my $result = $sth->fetch();
    if ($result) {
        print @$result;
        print "\n";
    }
    $sth->finish();
}

