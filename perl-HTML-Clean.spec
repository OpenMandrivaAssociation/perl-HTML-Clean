%define upstream_name	 HTML-Clean
%define upstream_version 0.8

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:	HTML shrinker
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
The HTML::Clean module encapsulates a number of HTML optimizations
and cleanups.  The end result is HTML that loads faster, displays
properly in more browsers.  Think of it as a compiler that
translates HTML input into optimized machine readable code.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%clean
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes README TODO
%{_bindir}/*
%{_mandir}/*/*
%{perl_vendorlib}/HTML
%{perl_vendorlib}/auto
