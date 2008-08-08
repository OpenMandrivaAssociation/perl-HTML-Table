%define real_name HTML-Table

Summary:	HTML::Table module for perl 
Name:		perl-%{real_name}
Version:	2.08
Release:	%mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
HTML::Table is used to generate HTML tables for CGI scripts.  By using the
methods provided fairly complex tables can be created, manipulated, then
printed from Perl scripts.  The module also greatly simplifies creating
tables within tables from Perl.  It is possible to create an entire table
using the methods provided and never use an HTML tag.

%prep

%setup -q -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/HTML/Table.pm
%{_mandir}/*/*


