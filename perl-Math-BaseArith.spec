#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	BaseArith
Summary:	Math::BaseArith - Perl extension for mixed-base number representation
Summary(pl):	Math::BaseArith - rozszerzenie Perla do reprezentacji liczb o ró¿nej podstawie
Name:		perl-Math-BaseArith
Version:	1.00
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The inspiration for this module is a pair of functions in the APL
programming language called encode (a.k.a. "representation") and
decode (a.k.a. base-value). Their principal use is to convert numbers
from one number base to another. Mixed number bases are permitted.

%description -l pl
Ten modu³ jest zainspirowany par± funkcji w jêzyku programowania APL o
nazwach encode (czyli "reprezentacja") oraz decode (warto¶æ bazowa).
Zasadnicze ich przeznaczenie to przeliczanie liczb z jednej podstawy
do innej. Dozwolone s± mieszane podstawy liczb.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Math/BaseArith.pm
%{_mandir}/man3/*
