%define module	HTML-Clean
%define version 0.8
%define release %mkrel 8

Summary:	HTML shrinker
Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source0:	%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%module/
Requires:	perl
BuildArch:	noarch

%description
The HTML::Clean module encapsulates a number of HTML optimizations
and cleanups.  The end result is HTML that loads faster, displays
properly in more browsers.  Think of it as a compiler that
translates HTML input into optimized machine readable code.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes README TODO
%{_bindir}/*
%{_mandir}/*/*
%{perl_vendorlib}/HTML
%{perl_vendorlib}/auto

