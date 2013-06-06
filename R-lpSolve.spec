%global packname  lpSolve
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          5.6.7
Release:          1
Summary:          Interface to Lp_solve v. 5.5 to solve linear/integer programs
Group:            Sciences/Mathematics
License:          LGPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/lpSolve_5.6.7.tar.gz
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    blas-devel
BuildRequires:    lapack-devel
Patch0:           lpSolve_5.6.7-format.patch

%description
Lp_solve is freely available (under LGPL 2) software for solving linear,
integer and mixed integer programs. In this implementation we supply a
"wrapper" function in C and some R functions that solve general
linear/integer problems, assignment problems, and transportation problems.
This version calls lp_solve version 5.5.

%prep
%setup -q -c -n %{packname}
%patch0 -p0

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs


%changelog
* Mon Feb 20 2012 Paulo Andrade <pcpa@mandriva.com.br> 5.6.6-1
+ Revision: 777869
- Import R-lpSolve
- Import R-lpSolve


