%define real_name HTML-Table

Summary:	HTML::Table module for perl 
Name:		perl-%{real_name}
Version:	2.08a
Release:	3
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




%changelog
* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 2.08a-2mdv2010.0
+ Revision: 440581
- rebuild

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.08a-1mdv2009.1
+ Revision: 292166
- update to new version 2.08a

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 2.08-2mdv2009.0
+ Revision: 268523
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.08-1mdv2009.0
+ Revision: 194856
- update to new version 2.08
- update to new version 2.08

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.06-1mdv2008.0
+ Revision: 46623
- update to new version 2.06

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 2.05-1mdv2008.0
+ Revision: 20138
- 2.05


* Fri Jan 26 2007 Oden Eriksson <oeriksson@mandriva.com> 2.04a-1mdv2007.0
+ Revision: 113848
- Import perl-HTML-Table

* Fri Jan 26 2007 Oden Eriksson <oeriksson@mandriva.com> 2.04a-1mdv2007.1
- 2.04a

* Tue Dec 13 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.03-1mdk
- 2.03

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 2.02-1mdk
- initial Mandriva package

