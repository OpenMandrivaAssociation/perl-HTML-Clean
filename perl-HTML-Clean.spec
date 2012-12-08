%define upstream_name	 HTML-Clean
%define upstream_version 0.8

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	HTML shrinker
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
The HTML::Clean module encapsulates a number of HTML optimizations
and cleanups.  The end result is HTML that loads faster, displays
properly in more browsers.  Think of it as a compiler that
translates HTML input into optimized machine readable code.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{_mandir}/*/*
%{perl_vendorlib}/HTML
%{perl_vendorlib}/auto


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.800.0-4mdv2012.0
+ Revision: 765301
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.800.0-3
+ Revision: 763842
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.800.0-2
+ Revision: 667192
- mass rebuild

* Fri Feb 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.800.0-1mdv2010.1
+ Revision: 504942
- rebuild using %%perl_convert_version

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.8-11mdv2010.0
+ Revision: 426497
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.8-10mdv2009.0
+ Revision: 223785
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.8-9mdv2008.1
+ Revision: 180405
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Apr 25 2007 Olivier Thauvin <nanardon@mandriva.org> 0.8-8mdv2008.0
+ Revision: 18068
- rebuild


* Wed Feb 15 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.8-7mdk
- rebuild, cleanup

* Wed Aug 13 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.8-6mdk
- rebuild for new perl
- drop Prefix tag
- don't use PREFIX
- drop $RPM_OPT_FLAGS, noarch..
- use %%makeinstall_std macro

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.8-5mdk
- rebuild for new auto{prov,req}

