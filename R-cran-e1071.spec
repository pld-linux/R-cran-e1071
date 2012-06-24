%define		fversion	%(echo %{version} |tr r -)
%define		modulename	e1071
Summary:	Misc Functions of the Department of Statistics (e1071), TU Wien
Summary(pl):	R�ne funkcje Wydzia�u Statystyki (e1071), Politechnika Wiede�ska
Name:		R-cran-%{modulename}
Version:	1.5r1
Release:	3
License:	GPL version 2. See COPYRIGHT.svm.cpp for the copyright of the svm C++ code.
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	5f0a033bb84d4be58575b3eb9549d53f
BuildRequires:	R-base >= 2.0.0
# should be BR: R-cran-class, but our builders doesn't support BR: foo after Provides: foo
BuildRequires:	R-cran-VR
Requires(post,postun):	R-base >= 2.0.0
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
Requires:	R-cran-class
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Functions for latent class analysis, short time Fourier transform,
fuzzy clustering, support vector machines, shortest path computation,
bagged clustering, naive Bayes classifier, ...

%description -l pl
Funkcje do analizy klas, szybkiej transformaty Fouriera, rozmytego
klastrowania, obs�ugi maszyn wektorowych, obliczenia najkr�tszych
�cie�ek, naiwnej klasyfikacji Baysa, ...

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%post
(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
 R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --htmllist)

%postun
if [ -f %{_libdir}/R/bin/Rcmd ];then
	(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
	R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --htmllist)
fi

%files
%defattr(644,root,root,755)
%doc %{modulename}/{DESCRIPTION,COPYRIGHT.*,NEWS,README}
%{_libdir}/R/library/%{modulename}
