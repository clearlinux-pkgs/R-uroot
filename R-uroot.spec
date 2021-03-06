#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-uroot
Version  : 2.1.2
Release  : 28
URL      : https://cran.r-project.org/src/contrib/uroot_2.1-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/uroot_2.1-2.tar.gz
Summary  : Unit Root Tests for Seasonal Time Series
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : buildreq-R

%description
P-values based on response surface regressions are available for both tests.
    P-values based on bootstrap are available for seasonal unit root tests.

%prep
%setup -q -c -n uroot
cd %{_builddir}/uroot

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1599609030

%install
export SOURCE_DATE_EPOCH=1599609030
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library uroot
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library uroot
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library uroot
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc uroot || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/uroot/DESCRIPTION
/usr/lib64/R/library/uroot/INDEX
/usr/lib64/R/library/uroot/Meta/Rd.rds
/usr/lib64/R/library/uroot/Meta/data.rds
/usr/lib64/R/library/uroot/Meta/features.rds
/usr/lib64/R/library/uroot/Meta/hsearch.rds
/usr/lib64/R/library/uroot/Meta/links.rds
/usr/lib64/R/library/uroot/Meta/nsInfo.rds
/usr/lib64/R/library/uroot/Meta/package.rds
/usr/lib64/R/library/uroot/Meta/vignette.rds
/usr/lib64/R/library/uroot/NAMESPACE
/usr/lib64/R/library/uroot/NEWS.md
/usr/lib64/R/library/uroot/R/sysdata.rdb
/usr/lib64/R/library/uroot/R/sysdata.rdx
/usr/lib64/R/library/uroot/R/uroot
/usr/lib64/R/library/uroot/R/uroot.rdb
/usr/lib64/R/library/uroot/R/uroot.rdx
/usr/lib64/R/library/uroot/data/Rdata.rdb
/usr/lib64/R/library/uroot/data/Rdata.rds
/usr/lib64/R/library/uroot/data/Rdata.rdx
/usr/lib64/R/library/uroot/doc/index.html
/usr/lib64/R/library/uroot/doc/uroot-intro.Rnw
/usr/lib64/R/library/uroot/doc/uroot-intro.pdf
/usr/lib64/R/library/uroot/help/AnIndex
/usr/lib64/R/library/uroot/help/aliases.rds
/usr/lib64/R/library/uroot/help/paths.rds
/usr/lib64/R/library/uroot/help/uroot.rdb
/usr/lib64/R/library/uroot/help/uroot.rdx
/usr/lib64/R/library/uroot/html/00Index.html
/usr/lib64/R/library/uroot/html/R.css
