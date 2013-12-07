%define modname	HTML-Clean
%define modver	0.8

Summary:	HTML shrinker
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	9
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/HTML/%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel

%description
The HTML::Clean module encapsulates a number of HTML optimizations
and cleanups.  The end result is HTML that loads faster, displays
properly in more browsers.  Think of it as a compiler that
translates HTML input into optimized machine readable code.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README TODO
%{_bindir}/*
%{perl_vendorlib}/HTML
%{perl_vendorlib}/auto
%{_mandir}/man1/*
%{_mandir}/man3/*

