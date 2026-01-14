#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Math
%define		pnam	BaseArith
Summary:	Math::BaseArith - Perl extension for mixed-base number representation
Summary(pl.UTF-8):	Math::BaseArith - rozszerzenie Perla do reprezentacji liczb o różnej podstawie
Name:		perl-Math-BaseArith
Version:	1.00
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4fb5ba50af1e8d83e0d442d4b950703c
URL:		http://search.cpan.org/dist/Math-BaseArith/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The inspiration for this module is a pair of functions in the APL
programming language called encode (a.k.a. "representation") and
decode (a.k.a. base-value). Their principal use is to convert numbers
from one number base to another. Mixed number bases are permitted.

%description -l pl.UTF-8
Ten moduł jest zainspirowany parą funkcji w języku programowania APL o
nazwach encode (czyli "reprezentacja") oraz decode (wartość bazowa).
Zasadnicze ich przeznaczenie to przeliczanie liczb z jednej podstawy
do innej. Dozwolone są mieszane podstawy liczb.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Math/BaseArith.pm
%{_mandir}/man3/*
