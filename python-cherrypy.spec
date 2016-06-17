%define tarname CherryPy-%{version}

Summary:        A Python-based framework for web application development
Name:           python-cherrypy
Version:        6.0.1
Release:        1
License:        BSD
Group:          Development/Python
URL:            http://www.cherrypy.org
Source0:        https://pypi.python.org/packages/22/57/7b2395e73821d17c9c73e67873dfecdd592f14ddff0af894f952245b5f55/CherryPy-%{version}.tar.gz
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python3-devel
BuildRequires:  python-setuptools
BuildArch:      noarch
%rename		python3-cherrypy

%description
A Python-based framework for web application development.

CheryPy allows you to write and easyly deploy web applications, thanks
to a bundled webserver. It features a automated way to map an url to a
mathod, allowing you to describe your site as a python class.

%package -n python2-cherrypy
Summary:        A Python-based framework for web application development
Group:          Development/Python
Requires:       python2
 
%description -n python2-cherrypy
A Python-based framework for web application development.

CheryPy allows you to write and easyly deploy web applications, thanks
to a bundled webserver. It features a automated way to map an url to a
mathod, allowing you to describe your site as a python class.

%prep
%setup -q -c

mv %{tarname} python2
cp -r python2 python3

%build
cat > tutorial.conf << EOF
[server]
socketPort = 8080
threadPool = 10

[session]
storageType=ram
EOF

pushd python2
cp ../tutorial.conf .
%{__python2} setup.py build
popd

pushd python3
cp ../tutorial.conf .
%{__python3} setup.py build
popd

%install
pushd python2
%{__python2} setup.py install --root=%{buildroot}
mv %{buildroot}/%{_bindir}/cherryd %{buildroot}/%{_bindir}/python2-cherryd
popd

pushd python3
%{__python3} setup.py install --root=%{buildroot} 
popd

%files -n python-cherrypy
%doc python3/cherrypy/tutorial/*
%{python_sitelib}/cherrypy/*
%{python_sitelib}/*.egg-info
%{_bindir}/cherryd

%files -n python2-cherrypy
%doc python2/cherrypy/tutorial/*
%{python2_sitelib}/cherrypy/*
%{python2_sitelib}/*.egg-info
%{_bindir}/python2-cherryd
