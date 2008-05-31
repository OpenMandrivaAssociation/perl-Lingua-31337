%define module   Lingua-31337
%define version    0.02
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    P3RL M0DU1E 7O c0NVer7 7ext 7O C0o1 741k
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Lingua/%{module}-%{version}.tar.gz
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
P3RL M0DU1E 7O c0NVer7 7ext 7O C0o1 741k.

%prep
%setup -q -n %{module}-%{version} 

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
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/Lingua

