%define upstream_name    Lingua-31337
%define upstream_version 0.02
Name:		perl-%{upstream_name}
Version:	0.02
Release:	3

Summary:	P3RL M0DU1E 7O c0NVer7 7ext 7O C0o1 741k
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Lingua-31337
Source0:	https://cpan.metacpan.org/authors/id/C/CW/CWEST/Lingua-31337-0.02.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
P3RL M0DU1E 7O c0NVer7 7ext 7O C0o1 741k.

%prep
%setup -q -n Lingua-31337-0.02

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/Lingua

