# TODO:
#   - do something with *.rdf file, there if file conflict with other lang packages
# UPDATING:
%if 0
rm -vf *.xpi
./builder -g
V=%{version}
U=http://releases.mozilla.org/pub/mozilla.org/firefox/releases/$V/linux-i686/
curl -s $U | sed -ne 's,.*href="\([^"]\+\)/".*,'"$U"'xpi/\1.xpi,p'
%endif

Summary:	Language packs for Firefox
Summary(pl.UTF-8):	Pakiety językowe dla Firefoksa
Name:		mozilla-firefox-languages
Version:	33.0.2
Release:	1
License:	MPL v2.0
Group:		I18n
Source0:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ach.xpi
# Source0-md5:	57d2c84275e11672f0fad8266296f707
Source1:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/af.xpi
# Source1-md5:	d8ac769b4f5ea83963ab7e0a5b9d03b2
Source2:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/an.xpi
# Source2-md5:	7661c3f21f2ebba2ac424a6361fe8ddd
Source3:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/az.xpi
# Source3-md5:	b940c14a8bb8f99586177f0ffaa6dd07
Source4:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ar.xpi
# Source4-md5:	831721152178945f9ed4439918860386
Source5:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/as.xpi
# Source5-md5:	95c54c21fea51eb78d563236a86d1012
Source6:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ast.xpi
# Source6-md5:	22351a86811aa462c4371186363f2349
Source7:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/be.xpi
# Source7-md5:	0a6fd9cd47dce9c5ca8ae2214a59e70c
Source8:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bg.xpi
# Source8-md5:	ebdac6da84f6b1c83a2c0b8666a8c04c
Source9:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bn-BD.xpi
# Source9-md5:	daa62481c18d81c3cc8f3315ccfabc2e
Source10:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bn-IN.xpi
# Source10-md5:	dd96e0e0afafb1e4b55cd0c73f29ce06
Source11:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/br.xpi
# Source11-md5:	4296565ee4449987b8681de0a9ef8612
Source12:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bs.xpi
# Source12-md5:	29d2a9ff827b400fd422339c3fe94213
Source13:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ca.xpi
# Source13-md5:	d3c130e00bd7f998eba381bb3e535867
Source14:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/cs.xpi
# Source14-md5:	2acb2ac7d8bf72b42a96443d1d412a7c
Source15:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/csb.xpi
# Source15-md5:	862a361b2387976da0319f069ee08872
Source16:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/cy.xpi
# Source16-md5:	16d1af761a3bb5e6d2bc3e3052c39faf
Source17:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/da.xpi
# Source17-md5:	882d5e5452782f768253e8749eaa275c
Source18:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/de.xpi
# Source18-md5:	ee4356a24c8a147ae393937206b348f3
Source19:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/dsb.xpi
# Source19-md5:	03631a11859e679a914abcfc0b6b3db2
Source20:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/el.xpi
# Source20-md5:	f6e4f480e63bcd83003c64256e1f8e60
Source21:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/en-GB.xpi
# Source21-md5:	89d6b51997b60bab58637cf2b91b4328
Source22:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/en-US.xpi
# Source22-md5:	df7abd1d1b711a67cdb7d63a389f1d47
Source23:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/en-ZA.xpi
# Source23-md5:	245d2630c7b67208e5326d2273f9cd6c
Source24:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/eo.xpi
# Source24-md5:	045b482a0dcb3e70118d952b449c1b00
Source25:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-AR.xpi
# Source25-md5:	ac740f57304dde52f60d3aa23949fe21
Source26:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-CL.xpi
# Source26-md5:	3fc011cab10aeb64a33721cd3f516b5e
Source27:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-ES.xpi
# Source27-md5:	af97dc0df755a213c5793dd6ccc9bc18
Source28:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-MX.xpi
# Source28-md5:	2fcfd46da73b201c2debd0beb13467f7
Source29:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/et.xpi
# Source29-md5:	41943b0f4fbfc39c8864adce770ce320
Source30:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/eu.xpi
# Source30-md5:	e91c5648b88b1b8adc7f1a1214081f29
Source31:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fa.xpi
# Source31-md5:	0962427670210c79b38ac6fa4fe24a6a
Source32:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ff.xpi
# Source32-md5:	92ad9fb2277a7a920e10c79fd699955a
Source33:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fi.xpi
# Source33-md5:	3b92d3fc1c91d96e9367b8e94383e3e3
Source34:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fr.xpi
# Source34-md5:	b67c6be70ddc8c9f989671a662c129d0
Source35:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fy-NL.xpi
# Source35-md5:	027660aaa01aa960d1c987886aa217d0
Source36:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ga-IE.xpi
# Source36-md5:	f51ceb71ada4981272700c38cad44c8f
Source37:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gd.xpi
# Source37-md5:	17acaba74e61cd8ea084a9b684af5af5
Source38:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gl.xpi
# Source38-md5:	8860c17b056e1a6b9832787a5f0c0373
Source39:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gu-IN.xpi
# Source39-md5:	0c675cbefc05c943b320baa8f1e2f789
Source40:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/he.xpi
# Source40-md5:	167d5fc44b90c02767e763b4249a84fb
Source41:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hi-IN.xpi
# Source41-md5:	bd7c62f228fc9fe9663a35723b77e0c1
Source42:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hr.xpi
# Source42-md5:	af5e1e672dcdd4c1b2a19690416b0789
Source43:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hsb.xpi
# Source43-md5:	6b75188e273c8f2e8910d3ac2eb871a2
Source44:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hu.xpi
# Source44-md5:	400f06533db3792ed2d343015dad600f
Source45:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hy-AM.xpi
# Source45-md5:	8afc0ce52648b107cf149bbb23286c4f
Source46:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/id.xpi
# Source46-md5:	4f31bfd6e2a67f81ba66a45d8b721213
Source47:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/is.xpi
# Source47-md5:	160a64277bf8a4567c4e9764f90cb31e
Source48:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/it.xpi
# Source48-md5:	db5cd27160468552be0dbc07df65743b
Source49:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ja.xpi
# Source49-md5:	92497aa95e25ced60c34c91c6d080c67
Source50:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/kk.xpi
# Source50-md5:	deaae386338f9d974ecb41cfe666c7cd
Source51:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/km.xpi
# Source51-md5:	81494751e1a93addfdea110b93dc5720
Source52:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/kn.xpi
# Source52-md5:	80e7f147f425ec9d3ddb88c628d5acea
Source53:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ko.xpi
# Source53-md5:	d815f361c00b0a5e4c80a632051b0eb1
Source54:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ku.xpi
# Source54-md5:	edcc3dd60613c97634baad9613b2287f
Source55:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lij.xpi
# Source55-md5:	8cff8b17e752912b02e3d5ef00bde63e
Source56:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lt.xpi
# Source56-md5:	3a7dfc47eeb9fee1811b748563e2fe87
Source57:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lv.xpi
# Source57-md5:	e37ab9b0f97b726f03d1ad647ffd0fd2
Source58:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/mai.xpi
# Source58-md5:	ae61f4272378916ae49a7b8deaf6cc0b
Source59:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/mk.xpi
# Source59-md5:	21eb2a7d8bd3e86bf13fde7f1433a158
Source60:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ml.xpi
# Source60-md5:	6178c2893c92b0fbc99fe19aa20c54b8
Source61:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/mr.xpi
# Source61-md5:	57a75939f642a3766304ee896326aa7e
Source62:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ms.xpi
# Source62-md5:	257e622924e9d2c9aa760df90ab1fd32
Source63:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nb-NO.xpi
# Source63-md5:	9ee7e225ee1957e6ad5b1123a8926b3f
Source64:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nl.xpi
# Source64-md5:	218cca929f40adf389775303c3195d64
Source65:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nn-NO.xpi
# Source65-md5:	e19afbb9c03db5a812a9d8941c079dfa
Source66:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/or.xpi
# Source66-md5:	dfa87103ff442fac5ec1b2a7314325b1
Source67:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pa-IN.xpi
# Source67-md5:	75bd4b1e588c3fb8112ff2ed562f6a74
Source68:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pl.xpi
# Source68-md5:	a391570d62c016c53f09389703083a37
Source69:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pt-BR.xpi
# Source69-md5:	5023fad32d2db92ea41f9fc82f835f14
Source70:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pt-PT.xpi
# Source70-md5:	2859f3d05ea83f44eddaa66a0aa66f59
Source71:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/rm.xpi
# Source71-md5:	7523a704e9f0ae47cb6b6418e447bf97
Source72:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ro.xpi
# Source72-md5:	564b8f3f6b82137561c7d9b009e58868
Source73:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ru.xpi
# Source73-md5:	6c051388eee2df78c94549e6daf85c50
Source74:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/si.xpi
# Source74-md5:	523ab5b146c58ad9be045ccfe9968ec1
Source75:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sk.xpi
# Source75-md5:	43db761c9fe3cf09bb2e40550a34573e
Source76:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sl.xpi
# Source76-md5:	ab1666a862a0affaa22a7e37dbf10374
Source77:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/son.xpi
# Source77-md5:	cb98a94b41f7ab95ff80b91fbfbf41b9
Source78:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sq.xpi
# Source78-md5:	13327ca22c4ca45e2cc62429b72a68ac
Source79:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sr.xpi
# Source79-md5:	caaa9ccf0c0ad262e1d77b5f29bc5593
Source80:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sv-SE.xpi
# Source80-md5:	4c178eb67aa4fba8c467866b8dedc78b
Source81:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ta.xpi
# Source81-md5:	cb5efcdcef5d39e77e5d1f7a95b2b94a
Source82:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/te.xpi
# Source82-md5:	436e57537e338912629770e8d7f55c8f
Source83:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/th.xpi
# Source83-md5:	c46d44220e992c5b3ca28a7aa59ed431
Source84:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/tr.xpi
# Source84-md5:	ba3dcee831ec3a3e4ac167652412e2e1
Source85:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/uk.xpi
# Source85-md5:	b914824fcce8e00dfcb66ae501a39016
Source86:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/vi.xpi
# Source86-md5:	4cfc1e1d884ad1bc7b853f5484a20380
Source87:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/xh.xpi
# Source87-md5:	b195789ee141f3bd5423e27d0716941f
Source88:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/zh-CN.xpi
# Source88-md5:	4ad633e6d6beee5224455921c2c3fe02
Source89:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/zh-TW.xpi
# Source89-md5:	78d69a6f5497fdfd2a3bc20ebf583a40
Source90:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/zu.xpi
# Source90-md5:	ce6610ea6ff16625a0c5caa194a7c4e4
URL:		http://www.mozilla.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		firefoxdir	%{_datadir}/mozilla-firefox

%description
Language packs for Firefox.

%description -l pl.UTF-8
Pakiety językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ach
Summary:	Acoli resources for Firefox
Summary(pl.UTF-8):	Pliki językowe aczoli dla Firefoksa
Group:		I18n
Requires:	mozilla-firefox >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ach
Acoli resources for Firefox.

%description -n mozilla-firefox-lang-ach -l pl.UTF-8
Pliki językowe aczoli dla Firefoksa.

%package -n mozilla-firefox-lang-af
Summary:	Afrikaans resources for Firefox
Summary(pl.UTF-8):	Afrykanerskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-af
Afrikaans resources for Firefox.

%description -n mozilla-firefox-lang-af -l pl.UTF-8
Afrykanerskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-an
Summary:	Aragonese resources for Firefox
Summary(pl.UTF-8):	Aragońskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-an
Aragonese resources for Firefox.

%description -n mozilla-firefox-lang-an -l pl.UTF-8
Aragońskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ar
Summary:	Arabic resources for Firefox
Summary(pl.UTF-8):	Arabskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ar
Arabic resources for Firefox.

%description -n mozilla-firefox-lang-ar -l pl.UTF-8
Arabskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-as
Summary:	Assamese resources for Firefox
Summary(pl.UTF-8):	Asamskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}

%description -n mozilla-firefox-lang-as
Assamese resources for Firefox.

%description -n mozilla-firefox-lang-as -l pl.UTF-8
Asamskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ast
Summary:	Asturian resources for Firefox
Summary(pl.UTF-8):	Asturyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ast
Asturian resources for Firefox.

%description -n mozilla-firefox-lang-ast -l pl.UTF-8
Asturyjskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-az
Summary:	Azerbaijani resources for Firefox
Summary(pl.UTF-8):	Azerskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	mozilla-firefox >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-az
Azerbaijani resources for Firefox.

%description -n mozilla-firefox-lang-az -l pl.UTF-8
Azerskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-be
Summary:	Belarusian resources for Firefox
Summary(pl.UTF-8):	Białoruskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-be
Belarusian resources for Firefox.

%description -n mozilla-firefox-lang-be -l pl.UTF-8
Białoruskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-bg
Summary:	Bulgarian resources for Firefox
Summary(pl.UTF-8):	Bułgarskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-bg
Bulgarian resources for Firefox.

%description -n mozilla-firefox-lang-bg -l pl.UTF-8
Bułgarskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-bn
Summary:	Bengali (Bangladesh) resources for Firefox
Summary(pl.UTF-8):	Bengalskie pliki językowe dla Firefoksa (wersja dla Bangladeszu)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-bn
Bengali (Bangladesh) resources for Firefox.

%description -n mozilla-firefox-lang-bn -l pl.UTF-8
Bengalskie pliki językowe dla Firefoksa (wersja dla Bangladeszu).

%package -n mozilla-firefox-lang-bn_IN
Summary:	Bengali (India) resources for Firefox
Summary(pl.UTF-8):	Bengalskie pliki językowe dla Firefoksa (wersja dla Indii)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-bn_IN
Bengali (India) resources for Firefox.

%description -n mozilla-firefox-lang-bn_IN -l pl.UTF-8
Bengalskie pliki językowe dla Firefoksa (wersja dla Indii).

%package -n mozilla-firefox-lang-br
Summary:	Breton resources for Firefox
Summary(pl.UTF-8):	Bretońskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-br
Breton resources for Firefox.

%description -n mozilla-firefox-lang-br -l pl.UTF-8
Bretońskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-bs
Summary:	Bosnian resources for Firefox
Summary(pl.UTF-8):	Bośniackie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-bs
Bosnian resources for Firefox.

%description -n mozilla-firefox-lang-bs -l pl.UTF-8
Bośniackie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ca
Summary:	Catalan resources for Firefox
Summary(ca.UTF-8):	Recursos catalans per Firefox
Summary(es.UTF-8):	Recursos catalanes para Firefox
Summary(pl.UTF-8):	Katalońskie pliki językowe dla Firefoksa
Group:		I18n
URL:		http://www.softcatala.org/projectes/mozilla/
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ca
Catalan resources for Firefox.

%description -n mozilla-firefox-lang-ca -l ca.UTF-8
Recursos catalans per Firefox.

%description -n mozilla-firefox-lang-ca -l es.UTF-8
Recursos catalanes para Firefox.

%description -n mozilla-firefox-lang-ca -l pl.UTF-8
Katalońskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-cs
Summary:	Czech resources for Firefox
Summary(pl.UTF-8):	Czeskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-cs
Czech resources for Firefox.

%description -n mozilla-firefox-lang-cs -l pl.UTF-8
Czeskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-csb
Summary:	Kashubian resources for Firefox
Summary(pl.UTF-8):	Kaszubskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-csb
Kashubian resources for Firefox.

%description -n mozilla-firefox-lang-csb -l pl.UTF-8
Kaszubskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-cy
Summary:	Welsh resources for Firefox
Summary(pl.UTF-8):	Walijskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-cy
Welsh resources for Firefox.

%description -n mozilla-firefox-lang-cy -l pl.UTF-8
Walijskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-da
Summary:	Danish resources for Firefox
Summary(pl.UTF-8):	Duńskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-da
Danish resources for Firefox.

%description -n mozilla-firefox-lang-da -l pl.UTF-8
Duńskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-de
Summary:	German resources for Firefox
Summary(pl.UTF-8):	Niemieckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-de
German resources for Firefox.

%description -n mozilla-firefox-lang-de -l pl.UTF-8
Niemieckie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-dsb
Summary:	Lower Sorbian resources for Firefox
Summary(pl.UTF-8):	Dolnołużyckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-dsb
Lower Sorbian resources for Firefox.

%description -n mozilla-firefox-lang-dsb -l pl.UTF-8
Dolnołużyckie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-el
Summary:	Greek resources for Firefox
Summary(pl.UTF-8):	Greckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-el
Greek resources for Firefox.

%description -n mozilla-firefox-lang-el -l pl.UTF-8
Greckie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-en_GB
Summary:	English (British) resources for Firefox
Summary(pl.UTF-8):	Angielskie (brytyjskie) pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-en_GB
English (British) resources for Firefox.

%description -n mozilla-firefox-lang-en_GB -l pl.UTF-8
Angielskie (brytyjskie) pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-en_US
Summary:	English (American) resources for Firefox
Summary(pl.UTF-8):	Angielskie (amerykańskie) pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-en_US
English (American) resources for Firefox.

%description -n mozilla-firefox-lang-en_US -l pl.UTF-8
Angielskie (amerykańskie) pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-en_ZA
Summary:	English (South Africa) resources for Firefox
Summary(pl.UTF-8):	Angielskie pliki językowe dla Firefoksa (wersja dla RPA)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-en_ZA
English (South Africa) resources for Firefox.

%description -n mozilla-firefox-lang-en_ZA -l pl.UTF-8
Angielskie pliki językowe dla Firefoksa (wersja dla Republiki
Południowej Afryki).

%package -n mozilla-firefox-lang-eo
Summary:	Esperanto resources for Firefox
Summary(pl.UTF-8):	Pliki językowe esperanto dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-eo
Esperanto resources for Firefox.

%description -n mozilla-firefox-lang-eo -l pl.UTF-8
Pliki językowe esperanto dla Firefoksa.

%package -n mozilla-firefox-lang-es_AR
Summary:	Spanish (Andorra) resources for Firefox
Summary(ca.UTF-8):	Recursos espanyols (Andorra) per Firefox
Summary(es.UTF-8):	Recursos españoles (Andorra) para Firefox
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Firefoksa (wersja dla Andory)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-es_AR
Spanish (Spain) resources for Firefox.

%description -n mozilla-firefox-lang-es_AR -l ca.UTF-8
Recursos espanyols (Andorra) per Firefox.

%description -n mozilla-firefox-lang-es_AR -l es.UTF-8
Recursos españoles (Andorra) para Firefox.

%description -n mozilla-firefox-lang-es_AR -l pl.UTF-8
Hiszpańskie pliki językowe dla Firefoksa (wersja dla Andory).

%package -n mozilla-firefox-lang-es_CL
Summary:	Spanish (Chile) resources for Firefox
Summary(ca.UTF-8):	Recursos espanyols (Xile) per Firefox
Summary(es.UTF-8):	Recursos españoles (Chile) para Firefox
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Firefoksa (wersja dla Chile)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-es_CL
Spanish (Chile) resources for Firefox.

%description -n mozilla-firefox-lang-es_CL -l ca.UTF-8
Recursos espanyols (Xile) per Firefox.

%description -n mozilla-firefox-lang-es_CL -l es.UTF-8
Recursos españoles (Chile) para Firefox.

%description -n mozilla-firefox-lang-es_CL -l pl.UTF-8
Hiszpańskie pliki językowe dla Firefoksa (wersja dla Chile).

%package -n mozilla-firefox-lang-es
Summary:	Spanish (Spain) resources for Firefox
Summary(ca.UTF-8):	Recursos espanyols (Espanya) per Firefox
Summary(es.UTF-8):	Recursos españoles (España) para Firefox
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Firefoksa (wersja dla Hiszpanii)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-es
Spanish (Spain) resources for Firefox.

%description -n mozilla-firefox-lang-es -l ca.UTF-8
Recursos espanyols (Espanya) per Firefox.

%description -n mozilla-firefox-lang-es -l es.UTF-8
Recursos españoles (España) para Firefox.

%description -n mozilla-firefox-lang-es -l pl.UTF-8
Hiszpańskie pliki językowe dla Firefoksa (wersja dla Hiszpanii).

%package -n mozilla-firefox-lang-es_MX
Summary:	Spanish (Mexico) resources for Firefox
Summary(ca.UTF-8):	Recursos espanyols (Mèxic) per Firefox
Summary(es.UTF-8):	Recursos españoles (México) para Firefox
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Firefoksa (wersja dla Meksyku)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-es_MX
Spanish (Mexico) resources for Firefox.

%description -n mozilla-firefox-lang-es_MX -l ca.UTF-8
Recursos espanyols (Mèxic) per Firefox.

%description -n mozilla-firefox-lang-es_MX -l es.UTF-8
Recursos españoles (México) para Firefox.

%description -n mozilla-firefox-lang-es_MX -l pl.UTF-8
Hiszpańskie pliki językowe dla Firefoksa (wersja dla Meksyku).

%package -n mozilla-firefox-lang-et
Summary:	Estonian resources for Firefox
Summary(pl.UTF-8):	Estońskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-et
Estonian resources for Firefox.

%description -n mozilla-firefox-lang-et -l pl.UTF-8
Estońskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-eu
Summary:	Basque resources for Firefox
Summary(pl.UTF-8):	Baskijskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-eu
Basque resources for Firefox.

%description -n mozilla-firefox-lang-eu -l pl.UTF-8
Baskijskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-fa
Summary:	Persian resources for Firefox
Summary(pl.UTF-8):	Perskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-fa
Persian resources for Firefox.

%description -n mozilla-firefox-lang-fa -l pl.UTF-8
Perskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ff
Summary:	Fulah resources for Firefox
Summary(pl.UTF-8):	Pliki językowe fulani dla Firefoksa
Group:		I18n
Requires:	mozilla-firefox >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ff
Fulah resources for Firefox.

%description -n mozilla-firefox-lang-ff -l pl.UTF-8
Pliki językowe fulani dla Firefoksa.

%package -n mozilla-firefox-lang-fi
Summary:	Finnish resources for Firefox
Summary(pl.UTF-8):	Fińskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-fi
Finnish resources for Firefox.

%description -n mozilla-firefox-lang-fi -l pl.UTF-8
Fińskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-fr
Summary:	French resources for Firefox
Summary(pl.UTF-8):	Francuskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-fr
French resources for Firefox.

%description -n mozilla-firefox-lang-fr -l pl.UTF-8
Francuskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-fy
Summary:	Frisian resources for Firefox
Summary(pl.UTF-8):	Fryzyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-fy
Frisian resources for Firefox.

%description -n mozilla-firefox-lang-fy -l pl.UTF-8
Fryzyjskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ga
Summary:	Irish resources for Firefox
Summary(pl.UTF-8):	Irlandzkie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ga
Irish resources for Firefox.

%description -n mozilla-firefox-lang-ga -l pl.UTF-8
Irlandzkie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-gd
Summary:	Gaelic resources for Firefox
Summary(pl.UTF-8):	Szkockie (gaelickie) pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-gd
Gaelic resources for Firefox.

%description -n mozilla-firefox-lang-gd -l pl.UTF-8
Szkockie (gaelickie) pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-gl
Summary:	Galician resources for Firefox
Summary(pl.UTF-8):	Galicyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-gl
Galician resources for Firefox.

%description -n mozilla-firefox-lang-gl -l pl.UTF-8
Galicyjskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-gu
Summary:	Gujarati resources for Firefox
Summary(pl.UTF-8):	Pliki językowe gudźarati dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-gu
Gujarati resources for Firefox.

%description -n mozilla-firefox-lang-gu -l pl.UTF-8
Pliki językowe gudźarati dla Firefoksa.

%package -n mozilla-firefox-lang-he
Summary:	Hebrew resources for Firefox
Summary(pl.UTF-8):	Hebrajskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-he
Hebrew resources for Firefox.

%description -n mozilla-firefox-lang-he -l pl.UTF-8
Hebrajskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-hi
Summary:	Hindi resources for Firefox
Summary(pl.UTF-8):	Pliki językowe hindi dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-hi
Hindi resources for Firefox.

%description -n mozilla-firefox-lang-hi -l pl.UTF-8
Pliki językowe hindi dla Firefoksa.

%package -n mozilla-firefox-lang-hr
Summary:	Croatian resources for Firefox
Summary(pl.UTF-8):	Chorwackie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-hr
Croatian resources for Firefox.

%description -n mozilla-firefox-lang-hr -l pl.UTF-8
Chorwackie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-hsb
Summary:	Upper Sorbian resources for Firefox
Summary(pl.UTF-8):	Górnołużyckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-hsb
Upper Sorbian resources for Firefox.

%description -n mozilla-firefox-lang-hsb -l pl.UTF-8
Górnołużyckie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-hu
Summary:	Hungarian resources for Firefox
Summary(hu.UTF-8):	Magyar nyelv Firefox-hez
Summary(pl.UTF-8):	Węgierskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-hu
Hungarian resources for Firefox.

%description -n mozilla-firefox-lang-hu -l hu.UTF-8
Magyar nyelv Firefox-hez.

%description -n mozilla-firefox-lang-hu -l pl.UTF-8
Węgierskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-hy
Summary:	Armenian resources for Firefox
Summary(pl.UTF-8):	Ormiańskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-hy
Armenian resources for Firefox.

%description -n mozilla-firefox-lang-hy -l pl.UTF-8
Ormiańskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-id
Summary:	Indonesian resources for Firefox
Summary(pl.UTF-8):	Indonezyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-id
Indonesian resources for Firefox.

%description -n mozilla-firefox-lang-id -l pl.UTF-8
Indonezyjskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-is
Summary:	Icelandic resources for Firefox
Summary(pl.UTF-8):	Islandzkie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-is
Icelandic resources for Firefox.

%description -n mozilla-firefox-lang-is -l pl.UTF-8
Islandzkie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-it
Summary:	Italian resources for Firefox
Summary(pl.UTF-8):	Włoskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-it
Italian resources for Firefox.

%description -n mozilla-firefox-lang-it -l pl.UTF-8
Włoskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ja
Summary:	Japanese resources for Firefox
Summary(pl.UTF-8):	Japońskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ja
Japanese resources for Firefox.

%description -n mozilla-firefox-lang-ja -l pl.UTF-8
Japońskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-kk
Summary:	Kazakh resources for Firefox
Summary(pl.UTF-8):	Kazachskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-kk
Kazakh resources for Firefox.

%description -n mozilla-firefox-lang-kk -l pl.UTF-8
Kazachskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-km
Summary:	Khmer resources for Firefox
Summary(pl.UTF-8):	Khmerskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	mozilla-firefox >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-km
Khmer resources for Firefox.

%description -n mozilla-firefox-lang-km -l pl.UTF-8
Khmerskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-kn
Summary:	Kannada resources for Firefox
Summary(pl.UTF-8):	Pliki językowe kannada dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-kn
Kannada resources for Firefox.

%description -n mozilla-firefox-lang-kn -l pl.UTF-8
Pliki językowe kannada dla Firefoksa.

%package -n mozilla-firefox-lang-ko
Summary:	Korean resources for Firefox
Summary(pl.UTF-8):	Koreańskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ko
Korean resources for Firefox.

%description -n mozilla-firefox-lang-ko -l pl.UTF-8
Koreańskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ku
Summary:	Kurdish resources for Firefox
Summary(pl.UTF-8):	Kurdyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ku
Kurdish resources for Firefox.

%description -n mozilla-firefox-lang-ku -l pl.UTF-8
Kurdyjskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-lij
Summary:	Ligurian resources for Firefox
Summary(pl.UTF-8):	Liguryjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	mozilla-firefox >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-lij
Ligurian resources for Firefox.

%description -n mozilla-firefox-lang-lij -l pl.UTF-8
Liguryjskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-lt
Summary:	Lithuanian resources for Firefox
Summary(pl.UTF-8):	Litewskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-lt
Lithuanian resources for Firefox.

%description -n mozilla-firefox-lang-lt -l pl.UTF-8
Litewskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-lv
Summary:	Latvian resources for Firefox
Summary(pl.UTF-8):	Łotewskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-lv
Latvian resources for Firefox.

%description -n mozilla-firefox-lang-lv -l pl.UTF-8
Łotewskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-mai
Summary:	Maithili resources for Firefox
Summary(pl.UTF-8):	Pliki językowe maithili dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-mai
Maithili resources for Firefox.

%description -n mozilla-firefox-lang-mai -l pl.UTF-8
Pliki językowe maithili dla Firefoksa.

%package -n mozilla-firefox-lang-mk
Summary:	Macedonian resources for Firefox
Summary(pl.UTF-8):	Macedońskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-mk
Macedonian resources for Firefox.

%description -n mozilla-firefox-lang-mk -l pl.UTF-8
Macedońskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ml
Summary:	Malayalam resources for Firefox
Summary(pl.UTF-8):	Pliki językowe malajalam dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ml
Malayalam resources for Firefox.

%description -n mozilla-firefox-lang-ml -l pl.UTF-8
Pliki językowe malajalam dla Firefoksa.

%package -n mozilla-firefox-lang-mr
Summary:	Marathi resources for Firefox
Summary(pl.UTF-8):	Pliki językowe marathi dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-mr
Marathi resources for Firefox.

%description -n mozilla-firefox-lang-mr -l pl.UTF-8
Pliki językowe marathi dla Firefoksa.

%package -n mozilla-firefox-lang-ms
Summary:	Malay resources for Firefox
Summary(pl.UTF-8):	Malajskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ms
Malay resources for Firefox.

%description -n mozilla-firefox-lang-ms -l pl.UTF-8
Malajskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-nb
Summary:	Norwegian Bokmaal resources for Firefox
Summary(pl.UTF-8):	Norweskie (bokmaal) pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-nb
Norwegian Bokmaal resources for Firefox.

%description -n mozilla-firefox-lang-nb -l pl.UTF-8
Norweskie (bokmaal) pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-nl
Summary:	Dutch resources for Firefox
Summary(pl.UTF-8):	Holenderskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-nl
Dutch resources for Firefox.

%description -n mozilla-firefox-lang-nl -l pl.UTF-8
Holenderskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-nn
Summary:	Norwegian Nynorsk resources for Firefox
Summary(pl.UTF-8):	Norweskie (nynorsk) pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-nn
Norwegian Nynorsk resources for Firefox.

%description -n mozilla-firefox-lang-nn -l pl.UTF-8
Norweskie (nynorsk) pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-or
Summary:	Oriya resources for Firefox
Summary(pl.UTF-8):	Pliki językowe orija dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-or
Oriya resources for Firefox.

%description -n mozilla-firefox-lang-or -l pl.UTF-8
Pliki językowe orija dla Firefoksa.

%package -n mozilla-firefox-lang-pa
Summary:	Panjabi resources for Firefox
Summary(pl.UTF-8):	Pendżabskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-pa
Panjabi resources for Firefox.

%description -n mozilla-firefox-lang-pa -l pl.UTF-8
Pendżabskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-pl
Summary:	Polish resources for Firefox
Summary(pl.UTF-8):	Polskie pliki językowe dla Firefoksa
Group:		I18n
URL:		http://www.firefox.pl/
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-pl
Polish resources for Firefox.

%description -n mozilla-firefox-lang-pl -l pl.UTF-8
Polskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-pt_BR
Summary:	Portuguese (Brazil) resources for Firefox
Summary(pl.UTF-8):	Portugalskie (brazylijskie) pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-pt_BR
Portuguese (Brazil) resources for Firefox.

%description -n mozilla-firefox-lang-pt_BR -l pl.UTF-8
Portugalskie (brazylijskie) pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-pt
Summary:	Portuguese (Portugal) resources for Firefox
Summary(pl.UTF-8):	Portugalskie pliki językowe dla Firefoksa (wersja dla Portugalii)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-pt
Portuguese (Portugal) resources for Firefox.

%description -n mozilla-firefox-lang-pt -l pl.UTF-8
Portugalskie pliki językowe dla Firefoksa (wersja dla Portugalii).

%package -n mozilla-firefox-lang-rm
Summary:	Romansh resources for Firefox
Summary(pl.UTF-8):	Retoromańskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-rm
Romansh resources for Firefox.

%description -n mozilla-firefox-lang-rm -l pl.UTF-8
Retoromańskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ro
Summary:	Romanian resources for Firefox
Summary(pl.UTF-8):	Rumuńskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ro
Romanian resources for Firefox.

%description -n mozilla-firefox-lang-ro -l pl.UTF-8
Rumuńskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ru
Summary:	Russian resources for Firefox
Summary(pl.UTF-8):	Rosyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ru
Russian resources for Firefox.

%description -n mozilla-firefox-lang-ru -l pl.UTF-8
Rosyjskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-si
Summary:	Sinhala resources for Firefox
Summary(pl.UTF-8):	Syngaleskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-si
Sinhala resources for Firefox.

%description -n mozilla-firefox-lang-si -l pl.UTF-8
Syngaleskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-sk
Summary:	Slovak resources for Firefox
Summary(pl.UTF-8):	Słowackie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-sk
Slovak resources for Firefox.

%description -n mozilla-firefox-lang-sk -l pl.UTF-8
Słowackie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-sl
Summary:	Slovene resources for Firefox
Summary(pl.UTF-8):	Słoweńskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-sl
Slovene resources for Firefox.

%description -n mozilla-firefox-lang-sl -l pl.UTF-8
Słoweńskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-son
Summary:	Songhai resources for Firefox
Summary(pl.UTF-8):	Songhajskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-son
Songhai resources for Firefox.

%description -n mozilla-firefox-lang-son -l pl.UTF-8
Songhajskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-sq
Summary:	Albanian resources for Firefox
Summary(pl.UTF-8):	Albańskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-sq
Albanian resources for Firefox.

%description -n mozilla-firefox-lang-sq -l pl.UTF-8
Albańskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-sr
Summary:	Serbian resources for Firefox
Summary(pl.UTF-8):	Serbskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-sr
Serbian resources for Firefox.

%description -n mozilla-firefox-lang-sr -l pl.UTF-8
Serbskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-sv
Summary:	Swedish resources for Firefox
Summary(pl.UTF-8):	Szwedzkie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-sv
Swedish resources for Firefox.

%description -n mozilla-firefox-lang-sv -l pl.UTF-8
Szwedzkie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ta
Summary:	Tamil (India) resources for Firefox
Summary(pl.UTF-8):	Tamilskie pliki językowe dla Firefoksa (wersja dla Indii)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ta
Tamil (India) resources for Firefox.

%description -n mozilla-firefox-lang-ta -l pl.UTF-8
Tamilskie pliki językowe dla Firefoksa (wersja dla Indii).

%package -n mozilla-firefox-lang-te
Summary:	Telugu resources for Firefox
Summary(pl.UTF-8):	Pliki językowe telugu dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-te
Telugu resources for Firefox.

%description -n mozilla-firefox-lang-te -l pl.UTF-8
Pliki językowe telugu dla Firefoksa.

%package -n mozilla-firefox-lang-th
Summary:	Thai resources for Firefox
Summary(pl.UTF-8):	Tajskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-th
Thai resources for Firefox.

%description -n mozilla-firefox-lang-th -l pl.UTF-8
Tajskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-tr
Summary:	Turkish resources for Firefox
Summary(pl.UTF-8):	Tureckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-tr
Turkish resources for Firefox.

%description -n mozilla-firefox-lang-tr -l pl.UTF-8
Tureckie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-uk
Summary:	Ukrainian resources for Firefox
Summary(pl.UTF-8):	Ukraińskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-uk
Ukrainian resources for Firefox.

%description -n mozilla-firefox-lang-uk -l pl.UTF-8
Ukraińskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-vi
Summary:	Vietmanese resources for Firefox
Summary(pl.UTF-8):	Wietnamskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-vi
Vietmanese resources for Firefox.

%description -n mozilla-firefox-lang-vi -l pl.UTF-8
Wietnamskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-xh
Summary:	Xhosa resources for Firefox
Summary(pl.UTF-8):	Pliki językowe xhosa dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-xh
Xhosa resources for Firefox.

%description -n mozilla-firefox-lang-xh -l pl.UTF-8
Pliki językowe xhosa dla Firefoksa.

%package -n mozilla-firefox-lang-zh_CN
Summary:	Simplified Chinese resources for Firefox
Summary(pl.UTF-8):	Chińskie (uproszczone) pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-zh_CN
Simplified Chinese resources for Firefox.

%description -n mozilla-firefox-lang-zh_CN -l pl.UTF-8
Chińskie uproszczone pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-zh_TW
Summary:	Traditional Chinese resources for Firefox
Summary(pl.UTF-8):	Chińskie tradycyjne pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-zh_TW
Traditional Chinese resources for Firefox.

%description -n mozilla-firefox-lang-zh_TW -l pl.UTF-8
Chińskie tradycyjne pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-zu
Summary:	Zulu resources for Firefox
Summary(pl.UTF-8):	Zuluskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-zu
Zulu resources for Firefox.

%description -n mozilla-firefox-lang-zu -l pl.UTF-8
Zuluskie pliki językowe dla Firefoksa.

%prep
unpack() {
    local args="$1" file="$2"
	local lang=$(basename $file .xpi)
	install -d $lang
	cd $lang
	cp -p $file .
	cd ..
}
%define __unzip unpack
%setup -qcT %(seq -f '-a %g' 0 90 | xargs)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{firefoxdir}/extensions
for a in */*.xpi; do
	basename=$(basename $a .xpi)
	cp -p $a $RPM_BUILD_ROOT%{firefoxdir}/extensions/langpack-$basename@firefox.mozilla.org.xpi
done

%clean
rm -rf $RPM_BUILD_ROOT

%files -n mozilla-firefox-lang-ach
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ach@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-af
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-af@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-an
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-an@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ar
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ar@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-as
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-as@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ast
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ast@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-az
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-az@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-be
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-be@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-bg
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-bg@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-bn
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-bn-BD@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-bn_IN
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-bn-IN@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-br
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-br@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-bs
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-bs@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ca
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ca@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-cs
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-cs@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-csb
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-csb@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-cy
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-cy@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-da
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-da@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-de
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-de@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-dsb
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-dsb@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-el
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-el@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-en_GB
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-en-GB@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-en_US
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-en-US@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-en_ZA
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-en-ZA@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-eo
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-eo@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-es_AR
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-es-AR@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-es_CL
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-es-CL@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-es
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-es-ES@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-es_MX
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-es-MX@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-et
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-et@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-eu
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-eu@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-fa
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-fa@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ff
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ff@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-fi
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-fi@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-fr
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-fr@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-fy
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-fy-NL@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ga
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ga-IE@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-gd
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-gd@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-gl
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-gl@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-gu
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-gu-IN@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-he
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-he@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-hi
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-hi-IN@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-hr
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-hr@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-hsb
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-hsb@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-hu
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-hu@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-hy
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-hy-AM@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-id
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-id@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-is
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-is@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-it
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-it@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ja
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ja@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-kk
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-kk@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-km
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-km@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-kn
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-kn@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ko
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ko@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ku
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ku@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-lij
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-lij@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-lt
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-lt@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-lv
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-lv@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-mai
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-mai@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-mk
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-mk@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ml
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ml@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-mr
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-mr@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ms
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ms@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-nb
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-nb-NO@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-nl
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-nl@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-nn
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-nn-NO@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-or
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-or@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-pa
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-pa-IN@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-pl
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-pl@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-pt_BR
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-pt-BR@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-pt
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-pt-PT@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-rm
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-rm@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ro
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ro@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ru
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ru@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-si
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-si@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-sk
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-sk@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-sl
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-sl@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-son
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-son@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-sq
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-sq@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-sr
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-sr@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-sv
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-sv-SE@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ta
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ta@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-te
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-te@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-th
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-th@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-tr
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-tr@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-uk
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-uk@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-vi
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-vi@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-xh
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-xh@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-zh_CN
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-zh-CN@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-zh_TW
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-zh-TW@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-zu
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-zu@firefox.mozilla.org.xpi
