#!/bin/perl

use DBI;

$user = "user1";
$password = "hello";

my $dbh = DBI->connect("DBI:MariaDB:test1", $user, $password) or die "Could not connect to database";

while(1) {
    print "> ";
    my $payload = <STDIN>;
    chomp($payload);
    if ($payload eq "exit") {
        last;
    }
    my $query = "SELECT * FROM person WHERE first_name = " . $payload;
    my $sth = $dbh->prepare($query);
    $sth->execute();
    my $result = $sth->fetch();
    if ($result) {
        print @$result;
        print "\n";
    }
    $sth->finish();
}

