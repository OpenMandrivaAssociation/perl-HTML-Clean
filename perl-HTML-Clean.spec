%define modname	HTML-Clean

Summary:	HTML shrinker
Name:		perl-%{modname}
Version:	1.4
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/HTML/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
The HTML::Clean module encapsulates a number of HTML optimizations
and cleanups.  The end result is HTML that loads faster, displays
properly in more browsers.  Think of it as a compiler that
translates HTML input into optimized machine readable code.

%prep
%autosetup -n %{modname}-%{version} -p1
%__perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" --skipdeps </dev/null

%build
%make_build

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

