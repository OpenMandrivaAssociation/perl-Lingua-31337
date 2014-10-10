%define upstream_name    Lingua-31337
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	P3RL M0DU1E 7O c0NVer7 7ext 7O C0o1 741k
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Lingua/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
P3RL M0DU1E 7O c0NVer7 7ext 7O C0o1 741k.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/Lingua

%changelog
* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.0
+ Revision: 402568
- update to 0.56

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.02-2mdv2009.0
+ Revision: 268538
- rebuild early 2009.0 package (before pixel changes)

* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-1mdv2009.0
+ Revision: 213736
- import perl-Lingua-31337


* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-1mdv2009.0
- first mdv release
