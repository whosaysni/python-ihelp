# coding: utf-8

ihelp = {
'': [
('32a09678744d9ed4032b21861e1bbc8b', True, 
"""組み込みの関数や例外、その他のオブジェクトです。

注意: None は `nil\' オブジェクトを表現します。また、 Ellipsis は
スライスの `...\' を表します。"""),

],

'__import__': [
('1fdf6ad2339b43aaa9e806fb04e9e758', True, 
"""__import__(name, globals={}, locals={}, fromlist=[], level=-1) -> module

モジュールを import します。引数 globals は import 時のコンテキストを決定
するためだけに使われ、変更されることはありません。 locals は今のところ
使われていません。 fromlist は ``from name import ...\'\' のエミュレーション
をするときの import する名前のリストです。
``import name\'\' をエミュレーションするときには、空のリストにします。
モジュールをパッケージから import する場合、 fromlist を空にしておくと
__import__(\'A.B\', ...) はパッケージ A を返します。 fromlist が空で
なければ、サブモジュール B を返します。 level は import の形式が絶対
import か、相対 import かを決めます。 -1 にすると、元々の import 戦略、
すなわち絶対と相対の両方の import を試みます。 0 にすると絶対 import のみ、
正の値にすると、現在のモジュールから指定した数だけ上のディレクトリからの
相対でモジュールを探します。"""),

],


'abs': [
('5a63c62ff7e52b116e5419a42adc8ff1', True, 
"""abs(number) -> number

number の絶対値を返します。"""),

],


'all': [
('2cc07c32dd84467faf018b6a004408de', True, 
"""all(iterable) -> bool

iterable のすべての要素 x について、 bool(x) が True である場合に
True を返します。"""),

],


'any': [
('bb0ccb4e57a641865cbfc8483b370cb2', True, 
"""any(iterable) -> bool

iterable のいずれかの要素 x について bool(x) が True のとき True を
返します。"""),

],


'apply': [
('2402fe405ffb73bfb2978f4291115166', True, 
"""apply(object[, args[, kwargs]]) -> value

呼び出し可能 (callable) なオブジェクト object を呼び出します。このとき、
args にタプルを指定すると固定引数として、 kwargs に辞書を指定すると
オプションのキーワード引数として使います。
クラスや、 __call__() メソッドを備えたインスタンスも callable です。

リリース 2.3 で撤廃されました。以下の構文:
    function(*args, **keywords)
で呼び出すようにしてください。"""),

],


'basestring': [
('bdd303322e33292f9013df6b3a865e44', True, 
"""basestring は直接インスタンス化できません。このクラスは str や unicode
のベースクラスです。"""),

],


'basestring.__eq__': [
('29276e56c1f9b89c0e4975783c563226', False, 
"""x.__eq__(y) <==> x==y"""),

],


'basestring.__ge__': [
('a40b7fe72a380879d7602be9b639db1b', False, 
"""x.__ge__(y) <==> x>=y"""),

],


'basestring.__getattribute__': [
('efa80438e88a77b4eba07ebe2d9ceb85', False, 
"""x.__getattribute__(\'name\') <==> x.name"""),

],


'basestring.__gt__': [
('43f3c9de3ba1d0a78dea8d37b57bff37', False, 
"""x.__gt__(y) <==> x>y"""),

],


'basestring.__hash__': [
('63a96d56ab20e8afcaf282823c66d409', False, 
"""x.__hash__() <==> hash(x)"""),

],


'basestring.__le__': [
('486eb7462a194cfb7ba27a685d3c6ec3', False, 
"""x.__le__(y) <==> x<=y"""),

],


'basestring.__lt__': [
('803809016499ca6afb70031b8fc55efe', False, 
"""x.__lt__(y) <==> x<y"""),

],


'basestring.__ne__': [
('1ffca5c8e0f2a871a1986db525d30469', False, 
"""x.__ne__(y) <==> x!=y"""),

],


'basestring.__repr__': [
('d7ecf995070b7d400aad745f917dd8f8', False, 
"""x.__repr__() <==> repr(x)"""),

],


'basestring.__str__': [
('5f53e31d167624726f84cafe0dfc5af2', False, 
"""x.__str__() <==> str(x)"""),

],


'bin': [
('8cf1448d9e4b355dff6119dce4710377', True, 
"""bin(number) -> string

整数や長整数型のバイナリ (二進) 表記を返します。"""),

],


'bool': [
('a7d2f35b0fac5fc95f55fc0a5f3c0c0e', True, 
"""bool(x) -> bool

引数 x の値が真値のときに True を、それ以外のときには False を返します。
bool 型のインスタンスは、組み込み定数 True か False しかありません。
bool 型は int 型のサブクラスで、これ以上サブクラス化できません。"""),

],


'buffer': [
('421cf93f9e1721af945f2b368a19ce5f', True, 
"""buffer(object [, offset[, size]])

引数に指定したオブジェクトを参照する、新たなバッファ (buffer) 
オブジェクトを生成します。生成されたバッファは、対象オブジェクトの
先頭から(または offset から) のスライスを参照します。このスライス
の範囲は、対象オブジェクトの末尾まで (または size に指定した長さまで) 
です。"""),

],


'buffer.__add__': [
('e6460aedb37b9d9bab7a60fb4f7dbaa6', False, 
"""x.__add__(y) <==> x+y"""),

],


'buffer.__delitem__': [
('367ba526f8846abe6af406894f245e61', False, 
"""x.__delitem__(y) <==> del x[y]"""),

],


'buffer.__delslice__': [
('2de10355c0a83a1b2eba238da976921b', True, 
"""x.__delslice__(i, j) <==> del x[i:j]

負のインデクスは使えません。"""),

],


'buffer.__getitem__': [
('5b1a2fedeaae4789f80b680bc5ab6529', False, 
"""x.__getitem__(y) <==> x[y]"""),

],


'buffer.__getslice__': [
('d8dc8374f2dd864544396f2f0b4f7f25', True, 
"""x.__getslice__(i, j) <==> x[i:j]

負のインデクスは使えません。"""),

],


'buffer.__len__': [
('3d6e075527d9b8e03b83a311002c24c1', False, 
"""x.__len__() <==> len(x)"""),

],


'buffer.__mul__': [
('81afa97dd875518810269060ffb7d938', False, 
"""x.__mul__(n) <==> x*n"""),

],


'buffer.__rmul__': [
('3705f779f36813dd93b82ce068898521', False, 
"""x.__rmul__(n) <==> n*x"""),

],


'buffer.__setitem__': [
('8c8d81a007fa9ee02ec1da163dab9ff7', False, 
"""x.__setitem__(i, y) <==> x[i]=y"""),

],


'buffer.__setslice__': [
('0832c2b634e3572f1700aa95e7190439', True, 
"""x.__setslice__(i, j, y) <==> x[i:j]=y

負のインデクスは使えません。"""),

],


'builtin_function_or_method.__new__': [
('12304ee59e00d00e0aded1076345767f', True, 
"""T.__new__(S, ...) -> T のサブタイプである型 S の新たなオブジェクトを
生成します"""),

],


'bytearray': [
('fef17e7caa366b8afac0be9eea787bc1', True, 
"""bytearray(iterable_of_ints) -> bytearray オブジェクト
bytearray(string, encoding[, errors]) -> bytearray オブジェクト
bytearray(bytes_or_bytearray) -> bytes_or_bytearray の変更可能なコピー
bytearray(memory_view) -> bytearray オブジェクト

以下の形式のデータから、変更可能なバイト列 (bytearray) を生成します。:
  - 値が range(256) の範囲の整数のリスト
  - 特定のエンコーディング方式でエンコードされた文字列
  - バイトアレイオブジェクト、またはバイトデータの列
  - バッファ (buffer) API を備えた任意のオブジェクト

bytearray(int) -> bytearray オブジェクト

指定した長さで、値がすべてゼロの bytearray を生成します。"""),

],


'bytearray.__add__': [
('e6460aedb37b9d9bab7a60fb4f7dbaa6', False, 
"""x.__add__(y) <==> x+y"""),

],


'bytearray.__alloc__': [
('7cbd0f318791497342e4a509721471a5', True, 
"""B.__alloc__() -> int

実際に確保したバイト数を返します。"""),

],


'bytearray.__contains__': [
('3e4d608788a476ebb6efff2e2c3258bf', False, 
"""x.__contains__(y) <==> y in x"""),

],


'bytearray.__delitem__': [
('367ba526f8846abe6af406894f245e61', False, 
"""x.__delitem__(y) <==> del x[y]"""),

],


'bytearray.__getitem__': [
('5b1a2fedeaae4789f80b680bc5ab6529', False, 
"""x.__getitem__(y) <==> x[y]"""),

],


'bytearray.__iadd__': [
('c6bf05c3c7c62466ba0e5fe88092ca3c', False, 
"""x.__iadd__(y) <==> x+=y"""),

],


'bytearray.__imul__': [
('716204859290aad65b3c9d6cf8b957f8', False, 
"""x.__imul__(y) <==> x*=y"""),

],


'bytearray.__iter__': [
('448f3e7033f2161670d1a383ba662d22', False, 
"""x.__iter__() <==> iter(x)"""),

],


'bytearray.__len__': [
('3d6e075527d9b8e03b83a311002c24c1', False, 
"""x.__len__() <==> len(x)"""),

],


'bytearray.__mul__': [
('81afa97dd875518810269060ffb7d938', False, 
"""x.__mul__(n) <==> x*n"""),

],


'bytearray.__reduce__': [
('588c3883072aa7e007926eb32098cdfc', True, 
"""pickle 化の際に使う状態情報を返します。"""),

],


'bytearray.__rmul__': [
('3705f779f36813dd93b82ce068898521', False, 
"""x.__rmul__(n) <==> n*x"""),

],


'bytearray.__setitem__': [
('8c8d81a007fa9ee02ec1da163dab9ff7', False, 
"""x.__setitem__(i, y) <==> x[i]=y"""),

],


'bytearray.__sizeof__': [
('d2c0505a2b8daa3826ee31a6ac9db82a', True, 
"""B.__sizeof__() -> int
 
B のメモリ上でのサイズをバイト単位で返します。"""),

],


'bytearray.append': [
('a2e70c76f07a1efe945fbe502d59c948', True, 
"""B.append(int) -> None

B の末尾に要素を一つ追加します。"""),

],


'bytearray.capitalize': [
('e1be8d98c25cd959a27fc02cdc0083da', True, 
"""B.capitalize() -> B のコピー

B のコピーを生成し、先頭の文字を (ASCII) で大文字にして返します。"""),

],


'bytearray.center': [
('edca5ef7f7627cd67cefbf9c197e6967', True, 
"""B.center(width[, fillchar]) -> B のコピー

B の両側に fillchar に指定した文字を追加して、幅が width で B が中央に
位置するような文字列を生成して返します。 fillchar を省略した場合、
スペースを代わりに使います。"""),

],


'bytearray.count': [
('709cb99d6d72e98664e84720a70f5571', True, 
"""B.count(sub [,start [,end]]) -> int

B[start:end] の中で、 sub 互いに重ならないで現れる数を計算して返します。
start と end はスライス表記と同じ方法で指定でき、省略するとそれぞれ
B の先頭と末尾を表します。"""),

],


'bytearray.decode': [
('69a0ba581a1ad0980126e4202946c78c', True, 
"""B.decode([encoding[, errors]]) -> unicode オブジェクト

encoding の名前で登録されている codec を使って、B をデコードして返し
ます。 encoding を省略すると、デフォルトエンコーディングを使います。
エラーを指定すると、デコード中に発生したエラーの処理スキームを変更
できます。デフォルトの設定は \'strict\' で、すべてのエンコーディング
エラーに対して UnicodeDecodeError を送出します。他には \'ignore\' と
\'replace\' を指定できます。また、 UnicodeDecodeError を処理できる
エラーハンドラを定義して codecs.register_error である名前で登録して
おけば、その名前も指定できます。"""),

],


'bytearray.endswith': [
('126783495a3104a6a5c7c38061c99be3', True, 
"""B.endswith(suffix [,start [,end]]) -> bool

B が suffix で終わる場合には True を、それ以外の場合には False を
返します。start を指定すると検索の開始位置を、 end を指定すると
検索の終了位置を指定できます。 suffix を文字列のタプルにすると、
複数の文字列を調べられます。"""),

],


'bytearray.expandtabs': [
('5963a1fc61248a57b630eb5bd445832d', True, 
"""B.expandtabs([tabsize]) -> B のコピー

S のコピーを生成し、S の中に含まれるすべてのタブ文字を複数のスペースに
変換して返します。 tabsize を指定しない場合、タブの幅を 8 スペースと
みなします。"""),

],


'bytearray.extend': [
('338f5bd1f30d1d8462a3d69ddcab9e9b', True, 
"""B.extend(iterable int) -> None

iterator のすべての要素を B の末尾に追加します。"""),

],


'bytearray.find': [
('d48c0928952bbe7ac9b9c282e5c76042', True, 
"""B.find(sub [,start [,end]]) -> int

B の中の範囲 s[start, end] で部分列 sub を探し、最初に見つかった
場所のインデクスを返します。 start と end は省略可能で、
スライス表記と同じ指定方法を使えます。

見つからなければ -1 を返します。"""),

],


'bytearray.fromhex': [
('1b6dc312ea220787a29dbc453d2bf0b9', True, 
"""bytearray.fromhex(string) -> bytearray

十六表記で数を表現している文字列からbytearray オブジェクトを生成
して返します。数の間にスペースが入っていてもかまいません。
例: bytearray.fromhex(\'B9 01EF\') -> bytearray(b\'\\\\xb9\\\\x01\\\\xef\')."""),

],


'bytearray.index': [
('ae6ac9d4e90ee419f62a15988ab877cc', True, 
"""B.index(sub [,start [,end]]) -> int

B.find() と似ていますが、 sub が見つからないときに ValueError を
送出します。"""),

],


'bytearray.insert': [
('1163ff4c92cfd5fb550bde72d399e423', True, 
"""B.insert(index, int) -> None

bytearray 中の index の直前に一つだけ要素を挿入します。"""),

],


'bytearray.isalnum': [
('8c38acd4254866e8ea191fa6c78ec2c6', True, 
"""B.isalnum() -> bool

B が少なくとも 1 文字からなり、そのすべての文字が英数字である場合
に True を返します。それ以外の場合には False を返します。"""),

],


'bytearray.isalpha': [
('60b1477d38a9078a831eefad1100eb21', True, 
"""B.isalpha() -> bool

B が少なくとも 1 文字からなり、そのすべての文字がアルファベットで
ある場合に True を返します。それ以外の場合には False を返します。
"""),

],


'bytearray.isdigit': [
('4ce2c71389c56280f232e0e5fa4ffb5b', True, 
"""B.isdigit() -> bool

B が少なくとも 1 文字からなり、そのすべての文字が数字である場合
に True を返します。それ以外の場合には False を返します。"""),

],


'bytearray.islower': [
('9f8f189da294972c0a21b5ca8361a233', True, 
"""B.islower() -> bool

B が少なくとも 1 文字からなり、そのすべての文字が小文字である場合
に True を返します。それ以外の場合には False を返します。"""),

],


'bytearray.isspace': [
('433e92a74d947365c28a18f675cc3791', True, 
"""B.isspace() -> bool

B が少なくとも 1 文字からなり、そのすべての文字が空白文字である場合
に True を返します。それ以外の場合には False を返します。"""),

],


'bytearray.istitle': [
('b5bd7b21e2ccf9863539b2967ed1cb40', True, 
"""B.istitle() -> bool

B が少なくとも 1 文字からなり、タイトルケースである場合、すなわち
先頭の文字が大文字で、それ以降の文字が小文字である場合に True を
返します。それ以外の場合には False を返します。"""),

],


'bytearray.isupper': [
('a7ddd86eddf7a1f8aa102c786f63a2ce', True, 
"""B.isupper() -> bool

B が少なくとも 1 文字からなり、そのすべての文字が大文字である場合
に True を返します。それ以外の場合には False を返します。"""),

],


'bytearray.join': [
('9b1e6747da19d19776acc6b4b8579b19', True, 
"""B.join(iterable_of_bytes) -> bytes

iterable_of_bytes の任意個数の bytearray オブジェクトを B で結合した
バイト列を生成して返します。"""),

],


'bytearray.ljust': [
('535ef9466aad50e5d8c747ec66d095fe', True, 
"""B.ljust(width[, fillchar]) -> B のコピー

B を幅 width の文字列中に左寄せに配置した文字列を生成して返します。
文字列は fillchar に指定した文字でパディングされます。 fillchar
を省略すると、スペースを使います。"""),

],


'bytearray.lower': [
('24dcff2bbfa8a4f7ac84d64114d2402c', True, 
"""B.lower() -> B のコピー

B のコピーを生成し、すべての ASCII 文字を小文字にして返します。"""),

],


'bytearray.lstrip': [
('866961c3bb71165cd59703b21b250fc8', True, 
"""B.lstrip([bytes]) -> bytearray

B のコピーを生成し、先頭から、引数 bytes に指定した文字を除去して
返します。引数を省略すると、先頭の ASCII 空白文字を除去します。"""),

],


'bytearray.partition': [
('79089b29a5ddad92d973d775426e67f7', True, 
"""B.partition(sep) -> (head, sep, tail)

S の中でセパレータ sep を探し、見つかった場合には、セパレータ
以前前の文字列、セパレータ本体、セパレータ以降の文字列からなる
タプルを返します。セパレータが見つからなかった場合には、 S と二つの
空の bytearray からなるタプルを返します。"""),

],


'bytearray.pop': [
('496fd18ba3d82a14d854cf682d8d5bbe', True, 
"""B.pop([index]) -> int

B の index の位置にある要素を一つ除去し、除去した要素を返します。
index を省略すると、末尾の値を pop します。"""),

],


'bytearray.remove': [
('f4191bb7f233b62fd2162a834b685f37', True, 
"""B.remove(int) -> None

B の中で int を探し、最初に見つかった要素をを除去します。"""),

],


'bytearray.replace': [
('4dc30d670406147d828936b16e597f45', True, 
"""B.replace(old, new[, count]) -> bytes

B のコピーを生成し、 old を new に置き換えて返します。オプションの
引数 count を指定した場合、先頭から count 回までで置き換えを止めます。"""),

],


'bytearray.reverse': [
('f2ed7e46ef9536d4e114422158f589e6', True, 
"""B.reverse() -> None

インプレースで B を逆順にします。"""),

],


'bytearray.rfind': [
('d3e9540adbba3e9ab82052a9f2d15ce5', True, 
"""B.rfind(sub [,start [,end]]) -> int

B の中で sub を探し、最後に見つかった位置のインデクスを返します。
sub の検索範囲は s[start,end] です。 start および end は
省略可能で、スライス表記と同じ方法で指定できます。

検索に失敗すると -1 を返します。"""),

],


'bytearray.rindex': [
('22437057d52ef2f8f35885cf7385ed20', True, 
"""B.rindex(sub [,start [,end]]) -> int

B.rfind() に似ていますが、見つからなかった場合に ValueError を送出
します。"""),

],


'bytearray.rjust': [
('ea189051f921be932d173cf69cd97b58', True, 
"""B.rjust(width[, fillchar]) -> B のコピー

B を幅 width の文字列中に右寄せに配置した文字列を生成して返します。
文字列は fillchar に指定した文字でパディングされます。 fillchar
を省略すると、スペースを使います。"""),

],


'bytearray.rpartition': [
('217979187519e5f9f11702e73871671c', True, 
"""B.rpartition(sep) -> (tail, sep, head)

S の中で末尾からセパレータ sep を探し、見つかった場合には、セパレータ
以前前の文字列、セパレータ本体、セパレータ以降の文字列からなる
タプルを返します。セパレータが見つからなかった場合には、 S と二つの
空の bytearray からなるタプルを返します。"""),

],


'bytearray.rsplit': [
('50ee60edae38b59b5f7cc13dd0d590aa', True, 
"""B.rsplit(sep[, maxsplit]) -> bytearray の list

引数 sep に含まれる文字を区切り文字として、 B を分割したリストを
生成して返します。分割は B の末尾から先頭に向けて実行されます。
sep を指定しない場合、 ASCII 空白文字 (スペース、タブ、復帰、改行、
行送り、水平タブ) を使って B を分割します。 maxsplit を指定すると、
maxsplit 個まで分割した時点で分割を止めます。"""),

],


'bytearray.rstrip': [
('6c5951f2c57a50aefdcf4953be18f054', True, 
"""B.rstrip([bytes]) -> bytearray

B の末尾から、 bytes に指定した文字を除去して返します。
bytes を省略すると、 ASCII 空白文字を除去します。"""),

],


'bytearray.split': [
('1437626f915464512ad71b9dfaa2da56', True, 
"""B.split([sep[, maxsplit]]) -> list of bytearray

引数 sep に含まれる文字を区切り文字として、 B を 分割したリストを
生成して返します。 sep を指定しない場合、 ASCII 空白文字 (スペース、
タブ、復帰、改行、行送り、水平タブ) を使って B を分割します。
maxsplit を指定すると、 maxsplit 個まで分割した時点で分割を
止めます。"""),

],


'bytearray.splitlines': [
('78662cbd9af80bf82f74bd9022dd0d85', True, 
"""B.splitlines([keepends]) -> 各行からなる list

B を改行で区切ったリストを返します。 keepends に True を指定しない
限り、リストには改行文字を含めません。"""),

],


'bytearray.startswith': [
('63a444b71fbd0fcc1ac68efc15edf3d5', True, 
"""B.startswith(prefix [,start [,end]]) -> bool

B の部分文字列が prefix に指定した文字列から開始する場合には True、
それ以外の場合には False を返します。引数 start と end には、検索の
開始位置と終了位置を指定します。省略すると、それぞれ B の先頭から
末尾までを調べます。 prefix には、調べたい複数の文字列をタプル
で指定できます。"""),

],


'bytearray.strip': [
('acd1c57ead04e27494fcf0b6a45fb0f1', True, 
"""B.strip([bytes]) -> bytearray

文字列の先頭と末尾から、 bytes に含まれる文字を除去します。
bytes 引数を省略した場合、 ASCII の空白文字を除去します。"""),

],


'bytearray.swapcase': [
('e074eeff4ad0c054d172ba79e1cbb3d9', True, 
"""B.swapcase() -> B のコピー

B のコピーを生成し、文字列中の ASCII 文字について、大文字は小文字に、
小文字は大文字にして返します。"""),

],


'bytearray.title': [
('38d0d5295ebb8762cbf249a9a5e7a7ae', True, 
"""B.title() -> B のコピー

B をタイトルケースに変換して返します。タイトルケースとは、先頭の文字が
大文字で、それ以降の文字がすべて小文字であるような文字列です。"""),

],


'bytearray.translate': [
('9f97aea14514c4b8808f5f5996c21497', True, 
"""B.translate(table[, deletechars]) -> bytearray

B のコピーを生成し、deletechars が指定されている場合には deletechars 
内に含まれる文字をすべて除去し、残りの文字について、変換テーブル
table に従って文字を変換して返します。
table は長さ 256 のバイト列でなければなりません。"""),

],


'bytearray.upper': [
('68d42fb3bf422d3cd60b3a3ff85024e6', True, 
"""B.upper() -> B のコピー

B のコピーを生成し、すべての ASCII 文字を大文字にして返します。"""),

],


'bytearray.zfill': [
('096db87e203ce6de61cac36aa93a3ce1', True, 
"""B.zfill(width) -> B のコピー

B の左側にゼロを追加して、全体で幅 width になるようにします。
B の幅が width 以下の場合でも、 B を切り詰めることはありません。"""),

],


'callable': [
('e0acb8d383fb97d31c4b546ff4ad5401', True, 
"""callable(object) -> bool

呼出し可能オブジェクト (関数など) かどうかを判定して返します。
クラスや、 __call__()  メソッドを持つインスタンスも呼出し可能です。"""),

],


'chr': [
('3aaa155c885a604312da168bc5d1768a', True, 
"""chr(i) -> character

序数が i の文字 1 つからなる文字列を返します。i の範囲は 0 <= i < 256 です。"""),

],


'classmethod': [
('95f48c0bd4b38e7292e7ec21ffac72e1', True, 
"""classmethod(function) -> method

関数をクラスメソッドに変換します。

インスタンスメソッドの第一引数にインスタンスを渡すように、
クラスメソッドの第一引数には、クラスを渡すことになっています。
クラスメソッドを宣言するには、以下のようなイディオムを使いましょう:

  class C:
      def f(cls, arg1, arg2, ...): ...
      f = classmethod(f)

クラスメソッドは、 (C.f() のような) クラスに対して呼び出す他に、
(C().f() のような) インスタンスに対しても呼び出せます。後者の場合、
クラスメソッドにはインスタンスのクラス以外の情報は渡りません。
クラスメソッドをサブクラスに対して呼び出すと、第一引数にはサブクラス
のクラスオブジェクトが渡されます。

クラスメソッドは C++ や Java の静的メソッドとは違います。
静的メソッドが必要なら、組込み関数 staticmethod を使ってください。"""),

],


'classmethod.__get__': [
('d26800418397c66c49e33dcfd65f7f03', False, 
"""descr.__get__(obj[, type]) -> value"""),

],


'cmp': [
('23a0ca9ed5143f718915877e0200e2bb', True, 
"""cmp(x, y) -> integer

x<y であれば負の値、 x==y ならゼロ、 x>y なら正の値を返します。"""),

],


'coerce': [
('685d93d5a33f50a6aee75c7cd6ff6d30', True, 
"""coerce(x, y) -> (x1, y1)

二つの数値型を引数にとり、それぞれの引数を共通の型に変換して、タプルに
して返します。変換には数値演算の際に使われるのと同じ規則が適用されます。
型強制が不可能なときには TypeError を送出します。"""),

],


'compile': [
('34d3939a9ebedafd4d19352c148e00c2', True, 
"""compile(source, filename, mode[, flags[, dont_inherit]]) -> code object

ソースコード文字列 (Python モジュールや実行文、式) をコンパイルして、
exec 文や eval() で実行可能なコードオブジェクトに変換します。
filename 引数は、実行時のエラーメッセージに使われます。
mode 引数は、モジュールをコンパイルする場合は \'exec\' に、単一の
(対話的に実行する) 式の場合は \'single\' に、式の場合には \'eval\' にします。
flags 引数を指定すると、コードのコンパイルにどの future 文を影響させる
かを制御できます。
dont_inherit 引数をゼロでない値にすると、 compile を呼び出す側の
コードで有効になっている future 文の効果をコンパイル処理に影響させません。
dont_inherit を省略したり、ゼロを指定すると、呼び出し側の future と、
明示的に指定した future の両方を考慮したコンパイルが実行されます。"""),

],


'complex': [
('8fdc26fdd4e52b9e7f6867c06caeadbb', True, 
"""complex(real[, imag]) -> complex number

引数に指定した実数部と虚数部 (省略可) から、複素数を生成します。
imag のデフォルト値を 0 としたときの (real + imag*1j) と同じです。"""),

],


'complex.__abs__': [
('f2abd704a5f550221ed980b2e2705c32', False, 
"""x.__abs__() <==> abs(x)"""),

],


'complex.__add__': [
('e6460aedb37b9d9bab7a60fb4f7dbaa6', False, 
"""x.__add__(y) <==> x+y"""),

],


'complex.__coerce__': [
('3d0dc814e0e5f1542dfcb94e85548628', False, 
"""x.__coerce__(y) <==> coerce(x, y)"""),

],


'complex.__div__': [
('4c99c4ef649797ccba5eac04ff19ddb2', False, 
"""x.__div__(y) <==> x/y"""),

],


'complex.__divmod__': [
('2b7d2620e0eea6f731d872ecd08e9db0', False, 
"""x.__divmod__(y) <==> divmod(x, y)"""),

],


'complex.__float__': [
('4fda8084fbf981f8ca05d3269cac8fff', False, 
"""x.__float__() <==> float(x)"""),

],


'complex.__floordiv__': [
('9a95fb992e47a548c67dd066dc18db92', False, 
"""x.__floordiv__(y) <==> x//y"""),

],


'complex.__getnewargs__': [
('d41d8cd98f00b204e9800998ecf8427e', False, 
""""""),

],


'complex.__int__': [
('4ce28b4400b621494ac706c935c68a5c', False, 
"""x.__int__() <==> int(x)"""),

],


'complex.__long__': [
('8c929f31b1228256035450345e93d7c8', False, 
"""x.__long__() <==> long(x)"""),

],


'complex.__mod__': [
('6833114697ac82c60289fa24897eabf0', False, 
"""x.__mod__(y) <==> x%y"""),

],


'complex.__mul__': [
('131e3ee8270a7e3a4eb3048963c3035f', False, 
"""x.__mul__(y) <==> x*y"""),

],


'complex.__neg__': [
('b8116e2ccb4eb620a227d47d5ade8aab', False, 
"""x.__neg__() <==> -x"""),

],


'complex.__nonzero__': [
('6ef831e34b2bd8389823930cdc5da741', False, 
"""x.__nonzero__() <==> x != 0"""),

],


'complex.__pos__': [
('a918e20eebd49d8da08d2c4fd79d3c2e', False, 
"""x.__pos__() <==> +x"""),

],


'complex.__pow__': [
('cf0ec3f8787ff00d59011db965541daf', False, 
"""x.__pow__(y[, z]) <==> pow(x, y[, z])"""),

],


'complex.__radd__': [
('b25ae2b25d815baf4bd20478a2a0f5fa', False, 
"""x.__radd__(y) <==> y+x"""),

],


'complex.__rdiv__': [
('cbbf46f634bdd2cf96890cdd6f6e8818', False, 
"""x.__rdiv__(y) <==> y/x"""),

],


'complex.__rdivmod__': [
('e0f8f012671ac842a6e3b5c1b626c425', False, 
"""x.__rdivmod__(y) <==> divmod(y, x)"""),

],


'complex.__rfloordiv__': [
('65d54e9fd86aeeaf263c3295725f8779', False, 
"""x.__rfloordiv__(y) <==> y//x"""),

],


'complex.__rmod__': [
('06f1130e0513ae2be0f9c61a70a181a4', False, 
"""x.__rmod__(y) <==> y%x"""),

],


'complex.__rmul__': [
('6ee329cd333c8616bca5d4eec3709a6d', False, 
"""x.__rmul__(y) <==> y*x"""),

],


'complex.__rpow__': [
('bcab33856c7f1ac53d2945d8680042a0', True, 
"""y.__rpow__(x[, z]) <==> pow(x, y[, z])"""),

],


'complex.__rsub__': [
('38c09ada0390bc15efda2fda66cf5bf0', True, 
"""x.__rsub__(y) <==> y-x"""),

],


'complex.__rtruediv__': [
('d27e2573016197cc6beff9a155d1a605', True, 
"""x.__rtruediv__(y) <==> y/x"""),

],


'complex.__sub__': [
('f311f7fcb90645e03097a51bf2c3ae3b', True, 
"""x.__sub__(y) <==> x-y"""),

],


'complex.__truediv__': [
('a3b7c4cb9a3324a0fef052ee4d9d94aa', True, 
"""x.__truediv__(y) <==> x/y"""),

],


'complex.conjugate': [
('2a74d1aaa72c84eeed0f96a5b66d7b10', True, 
"""complex.conjugate() -> complex

共役複素数を返します。 (3-4j).conjugate() == 3+4j です。"""),

],


'complex.imag': [
('d213520f337cea7606f1f1c12f1dc6b5', True, 
"""複素数の虚数部です。"""),

],


'complex.real': [
('72d30dc49502e1a2aa13e8eaa71c378e', True, 
"""複素数の実数部です。"""),

],


'delattr': [
('abfa80e4675ac0e02f0a4d094db82aac', True, 
"""delattr(object, name)

指定のアトリビュートをオブジェクトから除去します。 delattr(x, \'y\') は
``del x.y\'\' と同じです。"""),

],


'dict': [
('9238be977c1078e74c44b788df64ff12', True, 
"""dict() -> 新しい空の辞書
dict(mapping) -> 新しい辞書を生成し、 mapping オブジェクトのキー/値ペアを使って初期化します。
dict(seq) -> 新しい辞書を生成し、以下のような初期化を行います:
    d = {}
    for k, v in seq:
        d[k] = v
dict(**kwargs) -> 新しい辞書を生成し、キーワード引数リストの name=value ペア
    で初期化します。例えば、 dict(one=1, two=2) のように使います。"""),

],


'dict.__contains__': [
('3ae9b76c73affdb702443dd78fb6d5be', True, 
"""D.__contains__(k) -> D にキー k があれば True を、そうでなければ False を返します。"""),

],


'dict.__delitem__': [
('367ba526f8846abe6af406894f245e61', False, 
"""x.__delitem__(y) <==> del x[y]"""),

],


'dict.__getitem__': [
('5b1a2fedeaae4789f80b680bc5ab6529', False, 
"""x.__getitem__(y) <==> x[y]"""),

],


'dict.__iter__': [
('448f3e7033f2161670d1a383ba662d22', False, 
"""x.__iter__() <==> iter(x)"""),

],


'dict.__len__': [
('3d6e075527d9b8e03b83a311002c24c1', False, 
"""x.__len__() <==> len(x)"""),

],


'dict.__setitem__': [
('8c8d81a007fa9ee02ec1da163dab9ff7', False, 
"""x.__setitem__(i, y) <==> x[i]=y"""),

],


'dict.__sizeof__': [
('12ac8b3ffc4d31d93ee2c8dfd8fd858a', True, 
"""D.__sizeof__() -> D のメモリ上のサイズをバイト単位で返します"""),

],


'dict.clear': [
('9546c06e700fba8cdef2d89c2575c583', True, 
"""D.clear() -> None. D から全ての要素を除去します。"""),

],


'dict.copy': [
('1143fdf2e0ed3f535e98c885ff04df13', True, 
"""D.copy() -> D の浅いコピー"""),

],


'dict.fromkeys': [
('c8aca1752b1e4999fea4cf14631926d5', False, 
"""dict.fromkeys(S[,v]) -> New dict with keys from S and values equal to v.
v defaults to None."""),

],


'dict.get': [
('ad21d1fea6b5935438a580c62b681c93', False, 
"""D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None."""),

],


'dict.has_key': [
('2bd9db68d3dc63bd599247a9e5df09c1', False, 
"""D.has_key(k) -> True if D has a key k, else False"""),

],


'dict.items': [
('5dd74642fd0ff63f6f2ae972c3d9e3c5', False, 
"""D.items() -> list of D\'s (key, value) pairs, as 2-tuples"""),

],


'dict.iteritems': [
('3ff509be366199ffd446dd23a6161e08', False, 
"""D.iteritems() -> an iterator over the (key, value) items of D"""),

],


'dict.iterkeys': [
('cbde69c2e295dc6b80abb5a9a4279335', False, 
"""D.iterkeys() -> an iterator over the keys of D"""),

],


'dict.itervalues': [
('33b6e1124fa89630ccfb758fa12a19eb', False, 
"""D.itervalues() -> an iterator over the values of D"""),

],


'dict.keys': [
('36f2537aa81e7a32a3cb66082548de85', False, 
"""D.keys() -> list of D\'s keys"""),

],


'dict.pop': [
('e3bc5557355506f93dcd4bc6d19c70ec', False, 
"""D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised"""),

],


'dict.popitem': [
('cc789df112f946dedf181cb260a9ea65', False, 
"""D.popitem() -> (k, v), remove and return some (key, value) pair as a
2-tuple; but raise KeyError if D is empty."""),

],


'dict.setdefault': [
('3a8968f12c975ca01ec1da7f4900c2cf', False, 
"""D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D"""),

],


'dict.update': [
('cfdabf685ef7a5b48002b849c4b11fd1', True, 
"""D.update(E, **F) -> None.  D の要素を、辞書または iterable の
E と F で更新します。

E が .keys() メソッドを持つ場合には:     for k in E: D[k] = E[k]
E が .keys() メソッドを持たない場合:     for (k, v) in E: D[k] = v
です。どちらの場合も、続いて:            for k in F: D[k] = F[k]
を適用します。"""),

],


'dict.values': [
('4d952e41ba4471f0db851d49d232817c', False, 
"""D.values() -> list of D\'s values"""),

],


'dir': [
('7b0a438a8951a13885c4b4217185fca4', False, 
"""dir([object]) -> list of strings

If called without an argument, return the names in the current scope.
Else, return an alphabetized list of names comprising (some of) the attributes
of the given object, and of attributes reachable from it.
If the object supplies a method named __dir__, it will be used; otherwise
the default dir() logic is used and returns:
  for a module object: the module\'s attributes.
  for a class object:  its attributes, and recursively the attributes
    of its bases.
  for any other object: its attributes, its class\'s attributes, and
    recursively the attributes of its class\'s base classes."""),

],


'divmod': [
('5326c344b2ab3a384c588f19def9e91a', False, 
"""divmod(x, y) -> (div, mod)

Return the tuple ((x-x%y)/y, x%y).  Invariant: div*y + mod == x."""),

],


'enumerate': [
('cc07eb51e846c95be2600698c0ed7dd3', False, 
"""enumerate(iterable) -> iterator for index, value of iterable

Return an enumerate object.  iterable must be an other object that supports
iteration.  The enumerate object yields pairs containing a count (from
zero) and a value yielded by the iterable argument.  enumerate is useful
for obtaining an indexed list: (0, seq[0]), (1, seq[1]), (2, seq[2]), ..."""),

],


'enumerate.__iter__': [
('448f3e7033f2161670d1a383ba662d22', False, 
"""x.__iter__() <==> iter(x)"""),

],


'enumerate.next': [
('288fd681cdf3b0a8149971d514e6e91e', False, 
"""x.next() -> the next value, or raise StopIteration"""),

],


'eval': [
('cc8949b142666f83448b76f4bedf78e7', False, 
"""eval(source[, globals[, locals]]) -> value

Evaluate the source in the context of globals and locals.
The source may be a string representing a Python expression
or a code object as returned by compile().
The globals must be a dictionary and locals can be any mapping,
defaulting to the current globals and locals.
If only globals is given, locals defaults to it."""),

],


'execfile': [
('d0f3d6481e4e2e17c2389d7b4ede1b61', False, 
"""execfile(filename[, globals[, locals]])

Read and execute a Python script from a file.
The globals and locals are dictionaries, defaulting to the current
globals and locals.  If only globals is given, locals defaults to it."""),

],


'file': [
('71a981b5f58135192079e933ebc7b2fd', False, 
"""file(name[, mode[, buffering]]) -> file object

Open a file.  The mode can be \'r\', \'w\' or \'a\' for reading (default),
writing or appending.  The file will be created if it doesn\'t exist
when opened for writing or appending; it will be truncated when
opened for writing.  Add a \'b\' to the mode for binary files.
Add a \'+\' to the mode to allow simultaneous reading and writing.
If the buffering argument is given, 0 means unbuffered, 1 means line
buffered, and larger numbers specify the buffer size.  The preferred way
to open a file is with the builtin open() function.
Add a \'U\' to mode to open the file for input with universal newline
support.  Any line ending in the input file will be seen as a \'
\'
in Python.  Also, a file so opened gains the attribute \'newlines\';
the value for this attribute is one of None (no newline read yet),
\'\', \'
\', \'
\' or a tuple containing all the newline types seen.

\'U\' cannot be combined with \'w\' or \'+\' mode."""),

],


'file.__enter__': [
('6650896b429d1828f98343c5f90b9434', False, 
"""__enter__() -> self."""),

],


'file.__exit__': [
('8c3d5cb3db53c2f33621725ed4e3775c', False, 
"""__exit__(*excinfo) -> None.  Closes the file."""),

],


'file.__iter__': [
('448f3e7033f2161670d1a383ba662d22', False, 
"""x.__iter__() <==> iter(x)"""),

],


'file.close': [
('8b38a65ae37f66ea7ca0a021879b36bd', False, 
"""close() -> None or (perhaps) an integer.  Close the file.

Sets data attribute .closed to True.  A closed file cannot be used for
further I/O operations.  close() may be called more than once without
error.  Some kinds of file objects (for example, opened by popen())
may return an exit status upon closing."""),

],


'file.closed': [
('14d5a2d7f1ec9ff1baa73756826f5c5b', False, 
"""True if the file is closed"""),

],


'file.encoding': [
('03fd48cbb03f5346183895a3957456c6', False, 
"""file encoding"""),

],


'file.errors': [
('65f98260f2036a58b0409e6174ed5941', False, 
"""Unicode error handler"""),

],


'file.fileno': [
('b138ddbf7a5f8b336c74ec3bf4a08f41', False, 
"""fileno() -> integer \"file descriptor\".

This is needed for lower-level file interfaces, such os.read()."""),

],


'file.flush': [
('6d9a472a73bcd894996e47fb7cf6e231', False, 
"""flush() -> None.  Flush the internal I/O buffer."""),

],


'file.isatty': [
('83b5ece024d8d4e5b84579032ea19dce', False, 
"""isatty() -> true or false.  True if the file is connected to a tty device."""),

],


'file.mode': [
('6ed863ec0d41b88ff83148afb6565430', False, 
"""file mode (\'r\', \'U\', \'w\', \'a\', possibly with \'b\' or \'+\' added)"""),

],


'file.name': [
('652815cf98162e882bde2fc8c2103812', False, 
"""file name"""),

],


'file.newlines': [
('623ee3cbbdcd9e61f883fb7d4f785233', False, 
"""end-of-line convention used in this file"""),

],


'file.next': [
('288fd681cdf3b0a8149971d514e6e91e', False, 
"""x.next() -> the next value, or raise StopIteration"""),

],


'file.read': [
('c2ce7d0489e649ef6799714132cd48c1', False, 
"""read([size]) -> read at most size bytes, returned as a string.

If the size argument is negative or omitted, read until EOF is reached.
Notice that when in non-blocking mode, less data than what was requested
may be returned, even if no size parameter was given."""),

],


'file.readinto': [
('9cb9c29c58b05612f7cfac3381296711', False, 
"""readinto() -> Undocumented.  Don\'t use this; it may go away."""),

],


'file.readline': [
('e5e0d7abdcef0951b0c6248b166e408e', False, 
"""readline([size]) -> next line from the file, as a string.

Retain newline.  A non-negative size argument limits the maximum
number of bytes to return (an incomplete line may be returned then).
Return an empty string at EOF."""),

],


'file.readlines': [
('18093981824bed6dfd6c137be5987035', False, 
"""readlines([size]) -> list of strings, each a line from the file.

Call readline() repeatedly and return a list of the lines so read.
The optional size argument, if given, is an approximate bound on the
total number of bytes in the lines returned."""),

],


'file.seek': [
('eba52d16446dc1cd26d10330fb94ba3c', False, 
"""seek(offset[, whence]) -> None.  Move to new file position.

Argument offset is a byte count.  Optional argument whence defaults to
0 (offset from start of file, offset should be >= 0); other values are 1
(move relative to current position, positive or negative), and 2 (move
relative to end of file, usually negative, although many platforms allow
seeking beyond the end of a file).  If the file is opened in text mode,
only offsets returned by tell() are legal.  Use of other offsets causes
undefined behavior.
Note that not all file objects are seekable."""),

],


'file.softspace': [
('4bb402c4316f79ac3da9682929fd29c5', False, 
"""flag indicating that a space needs to be printed; used by print"""),

],


'file.tell': [
('3d170a45d592c2d112f0c5562020c31d', False, 
"""tell() -> current file position, an integer (may be a long integer)."""),

],


'file.truncate': [
('47064b4473ad0b4a829e730c43829c3f', False, 
"""truncate([size]) -> None.  Truncate the file to at most size bytes.

Size defaults to the current file position, as returned by tell()."""),

],


'file.write': [
('1af4b7aebe3cb207bbfe8a68d1fc69b2', False, 
"""write(str) -> None.  Write string str to file.

Note that due to buffering, flush() or close() may be needed before
the file on disk reflects the data written."""),

],


'file.writelines': [
('6e1ae37e2f03cf137294bf6f9f8bed07', False, 
"""writelines(sequence_of_strings) -> None.  Write the strings to the file.

Note that newlines are not added.  The sequence can be any iterable object
producing strings. This is equivalent to calling write() for each string."""),

],


'file.xreadlines': [
('b97ffc8dc0b6057be3c8d7a87e119d82', False, 
"""xreadlines() -> returns self.

For backward compatibility. File objects now include the performance
optimizations previously implemented in the xreadlines module."""),

],


'filter': [
('98015df23077266d4d0a2bfe0a1b029d', False, 
"""filter(function or None, sequence) -> list, tuple, or string

Return those items of sequence for which function(item) is true.  If
function is None, return the items that are true.  If sequence is a tuple
or string, return the same type, else return a list."""),

],


'float': [
('c902f5cce9a7e3acc1b6c327c84de0e2', False, 
"""float(x) -> floating point number

Convert a string or number to a floating point number, if possible."""),

],


'float.__abs__': [
('f2abd704a5f550221ed980b2e2705c32', False, 
"""x.__abs__() <==> abs(x)"""),

],


'float.__add__': [
('e6460aedb37b9d9bab7a60fb4f7dbaa6', False, 
"""x.__add__(y) <==> x+y"""),

],


'float.__coerce__': [
('3d0dc814e0e5f1542dfcb94e85548628', False, 
"""x.__coerce__(y) <==> coerce(x, y)"""),

],


'float.__div__': [
('4c99c4ef649797ccba5eac04ff19ddb2', False, 
"""x.__div__(y) <==> x/y"""),

],


'float.__divmod__': [
('2b7d2620e0eea6f731d872ecd08e9db0', False, 
"""x.__divmod__(y) <==> divmod(x, y)"""),

],


'float.__float__': [
('4fda8084fbf981f8ca05d3269cac8fff', False, 
"""x.__float__() <==> float(x)"""),

],


'float.__floordiv__': [
('9a95fb992e47a548c67dd066dc18db92', False, 
"""x.__floordiv__(y) <==> x//y"""),

],


'float.__format__': [
('944e5993f39b35e4d2b4d83a2a0d8420', False, 
"""float.__format__(format_spec) -> string

Formats the float according to format_spec."""),

],


'float.__getformat__': [
('c59142a12ff0d7f9641a347f23c79898', False, 
"""float.__getformat__(typestr) -> string

You probably don\'t want to use this function.  It exists mainly to be
used in Python\'s test suite.

typestr must be \'double\' or \'float\'.  This function returns whichever of
\'unknown\', \'IEEE, big-endian\' or \'IEEE, little-endian\' best describes the
format of floating point numbers used by the C type named by typestr."""),

],


'float.__getnewargs__': [
('d41d8cd98f00b204e9800998ecf8427e', False, 
""""""),

],


'float.__int__': [
('4ce28b4400b621494ac706c935c68a5c', False, 
"""x.__int__() <==> int(x)"""),

],


'float.__long__': [
('8c929f31b1228256035450345e93d7c8', False, 
"""x.__long__() <==> long(x)"""),

],


'float.__mod__': [
('6833114697ac82c60289fa24897eabf0', False, 
"""x.__mod__(y) <==> x%y"""),

],


'float.__mul__': [
('131e3ee8270a7e3a4eb3048963c3035f', False, 
"""x.__mul__(y) <==> x*y"""),

],


'float.__neg__': [
('b8116e2ccb4eb620a227d47d5ade8aab', False, 
"""x.__neg__() <==> -x"""),

],


'float.__nonzero__': [
('6ef831e34b2bd8389823930cdc5da741', False, 
"""x.__nonzero__() <==> x != 0"""),

],


'float.__pos__': [
('a918e20eebd49d8da08d2c4fd79d3c2e', False, 
"""x.__pos__() <==> +x"""),

],


'float.__pow__': [
('cf0ec3f8787ff00d59011db965541daf', False, 
"""x.__pow__(y[, z]) <==> pow(x, y[, z])"""),

],


'float.__radd__': [
('b25ae2b25d815baf4bd20478a2a0f5fa', False, 
"""x.__radd__(y) <==> y+x"""),

],


'float.__rdiv__': [
('cbbf46f634bdd2cf96890cdd6f6e8818', False, 
"""x.__rdiv__(y) <==> y/x"""),

],


'float.__rdivmod__': [
('e0f8f012671ac842a6e3b5c1b626c425', False, 
"""x.__rdivmod__(y) <==> divmod(y, x)"""),

],


'float.__rfloordiv__': [
('65d54e9fd86aeeaf263c3295725f8779', False, 
"""x.__rfloordiv__(y) <==> y//x"""),

],


'float.__rmod__': [
('06f1130e0513ae2be0f9c61a70a181a4', False, 
"""x.__rmod__(y) <==> y%x"""),

],


'float.__rmul__': [
('6ee329cd333c8616bca5d4eec3709a6d', False, 
"""x.__rmul__(y) <==> y*x"""),

],


'float.__rpow__': [
('bcab33856c7f1ac53d2945d8680042a0', False, 
"""y.__rpow__(x[, z]) <==> pow(x, y[, z])"""),

],


'float.__rsub__': [
('38c09ada0390bc15efda2fda66cf5bf0', False, 
"""x.__rsub__(y) <==> y-x"""),

],


'float.__rtruediv__': [
('d27e2573016197cc6beff9a155d1a605', False, 
"""x.__rtruediv__(y) <==> y/x"""),

],


'float.__setformat__': [
('d19332a09f4b6ada25f650296d3c1538', False, 
"""float.__setformat__(typestr, fmt) -> None

You probably don\'t want to use this function.  It exists mainly to be
used in Python\'s test suite.

typestr must be \'double\' or \'float\'.  fmt must be one of \'unknown\',
\'IEEE, big-endian\' or \'IEEE, little-endian\', and in addition can only be
one of the latter two if it appears to match the underlying C reality.

Overrides the automatic determination of C-level floating point type.
This affects how floats are converted to and from binary strings."""),

],


'float.__sub__': [
('f311f7fcb90645e03097a51bf2c3ae3b', False, 
"""x.__sub__(y) <==> x-y"""),

],


'float.__truediv__': [
('a3b7c4cb9a3324a0fef052ee4d9d94aa', False, 
"""x.__truediv__(y) <==> x/y"""),

],


'float.__trunc__': [
('afaf1bd4ef8cd31f70c0bd38393719e3', False, 
"""Returns the Integral closest to x between 0 and x."""),

],


'float.as_integer_ratio': [
('8c5516ac33b1dfe9ea034d1b5d6a9f85', False, 
"""float.as_integer_ratio() -> (int, int)

Returns a pair of integers, whose ratio is exactly equal to the original
float and with a positive denominator.
Raises OverflowError on infinities and a ValueError on NaNs.

>>> (10.0).as_integer_ratio()
(10, 1)
>>> (0.0).as_integer_ratio()
(0, 1)
>>> (-.25).as_integer_ratio()
(-1, 4)"""),

],


'float.conjugate': [
('ca11cc47264f8fc92a825f39b589f869', False, 
"""Returns self, the complex conjugate of any float."""),

],


'float.fromhex': [
('76fa5da011a42cde2dadd635ab49f037', False, 
"""float.fromhex(string) -> float

Create a floating-point number from a hexadecimal string.
>>> float.fromhex(\'0x1.ffffp10\')
2047.984375
>>> float.fromhex(\'-0x1p-1074\')
-4.9406564584124654e-324"""),

],


'float.hex': [
('f4c02f802d6978ec85829c386e1d402a', False, 
"""float.hex() -> string

Return a hexadecimal representation of a floating-point number.
>>> (-0.1).hex()
\'-0x1.999999999999ap-4\'
>>> 3.14159.hex()
\'0x1.921f9f01b866ep+1\'"""),

],


'float.imag': [
('d213520f337cea7606f1f1c12f1dc6b5', False, 
"""the imaginary part of a complex number"""),

],


'float.is_integer': [
('3b4797db718cdae933d3a0a53db09828', False, 
"""Returns True if the float is an integer."""),

],


'float.real': [
('72d30dc49502e1a2aa13e8eaa71c378e', False, 
"""the real part of a complex number"""),

],


'format': [
('3c16178038607341bda1d46a5a3d75bb', False, 
"""format(value[, format_spec]) -> string

Returns value.__format__(format_spec)
format_spec defaults to \"\""""),

],


'frozenset': [
('599b8604dc26a205cc6823eb41629254', False, 
"""frozenset(iterable) --> frozenset object

Build an immutable unordered collection of unique elements."""),

],


'frozenset.__and__': [
('34f22603582785806906d3a619fbff20', False, 
"""x.__and__(y) <==> x&y"""),

],


'frozenset.__contains__': [
('ffd9e4fc21822f7b05e9a9147e7ab5cb', False, 
"""x.__contains__(y) <==> y in x."""),

],


'frozenset.__iter__': [
('448f3e7033f2161670d1a383ba662d22', False, 
"""x.__iter__() <==> iter(x)"""),

],


'frozenset.__len__': [
('3d6e075527d9b8e03b83a311002c24c1', False, 
"""x.__len__() <==> len(x)"""),

],


'frozenset.__or__': [
('5aaa9cc7414a761ca43f7b6098059d20', False, 
"""x.__or__(y) <==> x|y"""),

],


'frozenset.__rand__': [
('4e31b1b862f6ec29e32800270e841ea4', False, 
"""x.__rand__(y) <==> y&x"""),

],


'frozenset.__reduce__': [
('588c3883072aa7e007926eb32098cdfc', False, 
"""Return state information for pickling."""),

],


'frozenset.__ror__': [
('da4d0348ca64c8c3d0aced68631472e6', False, 
"""x.__ror__(y) <==> y|x"""),

],


'frozenset.__rsub__': [
('38c09ada0390bc15efda2fda66cf5bf0', False, 
"""x.__rsub__(y) <==> y-x"""),

],


'frozenset.__rxor__': [
('70015a9fed00e657f349025f83450c30', False, 
"""x.__rxor__(y) <==> y^x"""),

],


'frozenset.__sizeof__': [
('e2b18bc0b4abb612dc21e3efe830695b', False, 
"""S.__sizeof__() -> size of S in memory, in bytes"""),

],


'frozenset.__sub__': [
('f311f7fcb90645e03097a51bf2c3ae3b', False, 
"""x.__sub__(y) <==> x-y"""),

],


'frozenset.__xor__': [
('6c6511aa3cefcc142940d3d29d9fc4dd', False, 
"""x.__xor__(y) <==> x^y"""),

],


'frozenset.copy': [
('42a24c7d25e5a9cfeeb1414761b60e42', False, 
"""Return a shallow copy of a set."""),

],


'frozenset.difference': [
('33b586d58256cd0addd07d52a35c3248', True, 
"""二つ以上の set インスタンスの間の差分 (difference) を、新たな set 
インスタンスとして返します。

(この set に含まれていて、引数の他の set に入っていない要素の集合を
返します。)"""),

],


'frozenset.intersection': [
('2fb7b3bddc0bd6ec5ecba2d509250429', False, 
"""Return the intersection of two sets as a new set.

(i.e. all elements that are in both sets.)"""),

],


'frozenset.isdisjoint': [
('a4982a4d169a3b3f6a46cd0f44c79bc7', False, 
"""Return True if two sets have a null intersection."""),

],


'frozenset.issubset': [
('88902362cc72f0758c8a79935b7d993c', False, 
"""Report whether another set contains this set."""),

],


'frozenset.issuperset': [
('5598fc98f1739ce2f114650df98889dd', False, 
"""Report whether this set contains another set."""),

],


'frozenset.symmetric_difference': [
('9fd3f2e18bffee87b7a970d97beb5b0d', False, 
"""Return the symmetric difference of two sets as a new set.

(i.e. all elements that are in exactly one of the sets.)"""),

],


'frozenset.union': [
('9a8f2a81d7820cbddf66d9b1c1f909ae', False, 
"""Return the union of sets as a new set.

(i.e. all elements that are in either set.)"""),

],


'getattr': [
('d273f8730be7bdc5f45b16413e73f8ef', False, 
"""getattr(object, name[, default]) -> value

Get a named attribute from an object; getattr(x, \'y\') is equivalent to x.y.
When a default argument is given, it is returned when the attribute doesn\'t
exist; without it, an exception is raised in that case."""),

],


'globals': [
('cbff4bf006c42e17dc834557e22fc96c', False, 
"""globals() -> dictionary

Return the dictionary containing the current scope\'s global variables."""),

],


'hasattr': [
('6e8546b4cb6a660ac3387f5fad64ae38', False, 
"""hasattr(object, name) -> bool

Return whether the object has an attribute with the given name.
(This is done by calling getattr(object, name) and catching exceptions.)"""),

],


'hash': [
('074494667471b81c2dbf96a66223c00c', False, 
"""hash(object) -> integer

Return a hash value for the object.  Two objects with the same value have
the same hash value.  The reverse is not necessarily true, but likely."""),

],


'hex': [
('21b67f0f8288972451b21f4e519538c5', False, 
"""hex(number) -> string

Return the hexadecimal representation of an integer or long integer."""),

],


'id': [
('f9a15e3318f9dba7b54ca570c7a73a99', False, 
"""id(object) -> integer

Return the identity of an object.  This is guaranteed to be unique among
simultaneously existing objects.  (Hint: it\'s the object\'s memory address.)"""),

],


'input': [
('860fdbd0e3317fa9b560c998b22b06e8', False, 
"""input([prompt]) -> value

Equivalent to eval(raw_input(prompt))."""),

],


'int': [
('66181a7e80b4d31aa1c682d8f09e08e9', False, 
"""int(x[, base]) -> integer

Convert a string or number to an integer, if possible.  A floating point
argument will be truncated towards zero (this does not include a string
representation of a floating point number!)  When converting a string, use
the optional base.  It is an error to supply a base when converting a
non-string.  If base is zero, the proper base is guessed based on the
string content.  If the argument is outside the integer range a
long object will be returned instead."""),

],


'int.__abs__': [
('f2abd704a5f550221ed980b2e2705c32', False, 
"""x.__abs__() <==> abs(x)"""),

],


'int.__add__': [
('e6460aedb37b9d9bab7a60fb4f7dbaa6', False, 
"""x.__add__(y) <==> x+y"""),

],


'int.__and__': [
('34f22603582785806906d3a619fbff20', False, 
"""x.__and__(y) <==> x&y"""),

],


'int.__coerce__': [
('3d0dc814e0e5f1542dfcb94e85548628', False, 
"""x.__coerce__(y) <==> coerce(x, y)"""),

],


'int.__div__': [
('4c99c4ef649797ccba5eac04ff19ddb2', False, 
"""x.__div__(y) <==> x/y"""),

],


'int.__divmod__': [
('2b7d2620e0eea6f731d872ecd08e9db0', False, 
"""x.__divmod__(y) <==> divmod(x, y)"""),

],


'int.__float__': [
('4fda8084fbf981f8ca05d3269cac8fff', False, 
"""x.__float__() <==> float(x)"""),

],


'int.__floordiv__': [
('9a95fb992e47a548c67dd066dc18db92', False, 
"""x.__floordiv__(y) <==> x//y"""),

],


'int.__format__': [
('d41d8cd98f00b204e9800998ecf8427e', False, 
""""""),

],


'int.__getnewargs__': [
('d41d8cd98f00b204e9800998ecf8427e', False, 
""""""),

],


'int.__hex__': [
('90d697452be414d8975c8d8c6f7a2555', False, 
"""x.__hex__() <==> hex(x)"""),

],


'int.__index__': [
('41003bb787667a27a886984ca53d92e4', False, 
"""x[y:z] <==> x[y.__index__():z.__index__()]"""),

],


'int.__int__': [
('4ce28b4400b621494ac706c935c68a5c', False, 
"""x.__int__() <==> int(x)"""),

],


'int.__invert__': [
('fe2ef705f0edf495578f68b26139508a', False, 
"""x.__invert__() <==> ~x"""),

],


'int.__long__': [
('8c929f31b1228256035450345e93d7c8', False, 
"""x.__long__() <==> long(x)"""),

],


'int.__lshift__': [
('caddc2d6a334913487a8ae40dde8f2ba', False, 
"""x.__lshift__(y) <==> x<<y"""),

],


'int.__mod__': [
('6833114697ac82c60289fa24897eabf0', False, 
"""x.__mod__(y) <==> x%y"""),

],


'int.__mul__': [
('131e3ee8270a7e3a4eb3048963c3035f', False, 
"""x.__mul__(y) <==> x*y"""),

],


'int.__neg__': [
('b8116e2ccb4eb620a227d47d5ade8aab', False, 
"""x.__neg__() <==> -x"""),

],


'int.__nonzero__': [
('6ef831e34b2bd8389823930cdc5da741', False, 
"""x.__nonzero__() <==> x != 0"""),

],


'int.__oct__': [
('665bf5f8194659353210e20cbcb48754', False, 
"""x.__oct__() <==> oct(x)"""),

],


'int.__or__': [
('5aaa9cc7414a761ca43f7b6098059d20', False, 
"""x.__or__(y) <==> x|y"""),

],


'int.__pos__': [
('a918e20eebd49d8da08d2c4fd79d3c2e', False, 
"""x.__pos__() <==> +x"""),

],


'int.__pow__': [
('cf0ec3f8787ff00d59011db965541daf', False, 
"""x.__pow__(y[, z]) <==> pow(x, y[, z])"""),

],


'int.__radd__': [
('b25ae2b25d815baf4bd20478a2a0f5fa', False, 
"""x.__radd__(y) <==> y+x"""),

],


'int.__rand__': [
('4e31b1b862f6ec29e32800270e841ea4', False, 
"""x.__rand__(y) <==> y&x"""),

],


'int.__rdiv__': [
('cbbf46f634bdd2cf96890cdd6f6e8818', False, 
"""x.__rdiv__(y) <==> y/x"""),

],


'int.__rdivmod__': [
('e0f8f012671ac842a6e3b5c1b626c425', False, 
"""x.__rdivmod__(y) <==> divmod(y, x)"""),

],


'int.__repr__': [
('d7ecf995070b7d400aad745f917dd8f8', False, 
"""x.__repr__() <==> repr(x)"""),

],


'int.__rfloordiv__': [
('65d54e9fd86aeeaf263c3295725f8779', False, 
"""x.__rfloordiv__(y) <==> y//x"""),

],


'int.__rlshift__': [
('f6da8b5ae2cf6302760201a17cae0f59', False, 
"""x.__rlshift__(y) <==> y<<x"""),

],


'int.__rmod__': [
('06f1130e0513ae2be0f9c61a70a181a4', False, 
"""x.__rmod__(y) <==> y%x"""),

],


'int.__rmul__': [
('6ee329cd333c8616bca5d4eec3709a6d', False, 
"""x.__rmul__(y) <==> y*x"""),

],


'int.__ror__': [
('da4d0348ca64c8c3d0aced68631472e6', False, 
"""x.__ror__(y) <==> y|x"""),

],


'int.__rpow__': [
('bcab33856c7f1ac53d2945d8680042a0', False, 
"""y.__rpow__(x[, z]) <==> pow(x, y[, z])"""),

],


'int.__rrshift__': [
('1086736a2257659a74d27eb32075a046', False, 
"""x.__rrshift__(y) <==> y>>x"""),

],


'int.__rshift__': [
('4747cfab9ec34d9f8bf93576a3c56410', False, 
"""x.__rshift__(y) <==> x>>y"""),

],


'int.__rsub__': [
('38c09ada0390bc15efda2fda66cf5bf0', False, 
"""x.__rsub__(y) <==> y-x"""),

],


'int.__rtruediv__': [
('d27e2573016197cc6beff9a155d1a605', False, 
"""x.__rtruediv__(y) <==> y/x"""),

],


'int.__rxor__': [
('70015a9fed00e657f349025f83450c30', False, 
"""x.__rxor__(y) <==> y^x"""),

],


'int.__str__': [
('5f53e31d167624726f84cafe0dfc5af2', False, 
"""x.__str__() <==> str(x)"""),

],


'int.__sub__': [
('f311f7fcb90645e03097a51bf2c3ae3b', False, 
"""x.__sub__(y) <==> x-y"""),

],


'int.__truediv__': [
('a3b7c4cb9a3324a0fef052ee4d9d94aa', False, 
"""x.__truediv__(y) <==> x/y"""),

],


'int.__trunc__': [
('5f7705c348f8ea982f2cc17fa738baf3', False, 
"""Truncating an Integral returns itself."""),

],


'int.__xor__': [
('6c6511aa3cefcc142940d3d29d9fc4dd', False, 
"""x.__xor__(y) <==> x^y"""),

],


'int.conjugate': [
('f31d9f22875e308ab4b2df12f8d1f29e', False, 
"""Returns self, the complex conjugate of any int."""),

],


'int.denominator': [
('58dade7e0e5478df7f26c0765e432ac2', False, 
"""the denominator of a rational number in lowest terms"""),

],


'int.imag': [
('d213520f337cea7606f1f1c12f1dc6b5', False, 
"""the imaginary part of a complex number"""),

],


'int.numerator': [
('f508b9e2647828fea347ac4759c7aaca', False, 
"""the numerator of a rational number in lowest terms"""),

],


'int.real': [
('72d30dc49502e1a2aa13e8eaa71c378e', False, 
"""the real part of a complex number"""),

],


'intern': [
('49b1eb0e64b5a2f1e8421b30666f8d9b', False, 
"""intern(string) -> string

``Intern\'\' the given string.  This enters the string in the (global)
table of interned strings whose purpose is to speed up dictionary lookups.
Return the string itself or the previously interned string object with the
same value."""),

],


'isinstance': [
('1e95dca5ed74f1c3efc0fb6ee4ef55d2', False, 
"""isinstance(object, class-or-type-or-tuple) -> bool

Return whether an object is an instance of a class or of a subclass thereof.
With a type as second argument, return whether that is the object\'s type.
The form using a tuple, isinstance(x, (A, B, ...)), is a shortcut for
isinstance(x, A) or isinstance(x, B) or ... (etc.)."""),

],


'issubclass': [
('ece0a082b7efc73fc8dd4acf2c11ee3d', False, 
"""issubclass(C, B) -> bool

Return whether class C is a subclass (i.e., a derived class) of class B.
When using a tuple as the second argument issubclass(X, (A, B, ...)),
is a shortcut for issubclass(X, A) or issubclass(X, B) or ... (etc.)."""),

],


'iter': [
('b4f0878fe6ed6e77e4c188d038605b58', False, 
"""iter(collection) -> iterator
iter(callable, sentinel) -> iterator

Get an iterator from an object.  In the first form, the argument must
supply its own iterator, or be a sequence.
In the second form, the callable is called until it returns the sentinel."""),

],


'len': [
('6ba1daabc627f48853f6cd6700a8f888', False, 
"""len(object) -> integer

Return the number of items of a sequence or mapping."""),

],


'list': [
('be57dfea4f5486206da60b0a9a868e15', False, 
"""list() -> 新しい list
list(sequence) -> 配列 sequence の要素を持つ新しい list インスタンス"""),

],


'list.__add__': [
('e6460aedb37b9d9bab7a60fb4f7dbaa6', False, 
"""x.__add__(y) <==> x+y"""),

],


'list.__contains__': [
('3e4d608788a476ebb6efff2e2c3258bf', False, 
"""x.__contains__(y) <==> y in x"""),

],


'list.__delitem__': [
('367ba526f8846abe6af406894f245e61', False, 
"""x.__delitem__(y) <==> del x[y]"""),

],


'list.__delslice__': [
('2de10355c0a83a1b2eba238da976921b', False, 
"""x.__delslice__(i, j) <==> del x[i:j]

Use of negative indices is not supported."""),

],


'list.__getitem__': [
('5b1a2fedeaae4789f80b680bc5ab6529', False, 
"""x.__getitem__(y) <==> x[y]"""),

],


'list.__getslice__': [
('d8dc8374f2dd864544396f2f0b4f7f25', False, 
"""x.__getslice__(i, j) <==> x[i:j]

Use of negative indices is not supported."""),

],


'list.__iadd__': [
('c6bf05c3c7c62466ba0e5fe88092ca3c', False, 
"""x.__iadd__(y) <==> x+=y"""),

],


'list.__imul__': [
('716204859290aad65b3c9d6cf8b957f8', False, 
"""x.__imul__(y) <==> x*=y"""),

],


'list.__iter__': [
('448f3e7033f2161670d1a383ba662d22', False, 
"""x.__iter__() <==> iter(x)"""),

],


'list.__len__': [
('3d6e075527d9b8e03b83a311002c24c1', False, 
"""x.__len__() <==> len(x)"""),

],


'list.__mul__': [
('81afa97dd875518810269060ffb7d938', False, 
"""x.__mul__(n) <==> x*n"""),

],


'list.__reversed__': [
('5edb67250d2d63cdacb85838c2b532b3', True, 
"""L.__reversed__() -- リストの内容を逆順に返すイテレータを返します"""),

],


'list.__rmul__': [
('3705f779f36813dd93b82ce068898521', False, 
"""x.__rmul__(n) <==> n*x"""),

],


'list.__setitem__': [
('8c8d81a007fa9ee02ec1da163dab9ff7', False, 
"""x.__setitem__(i, y) <==> x[i]=y"""),

],


'list.__setslice__': [
('0832c2b634e3572f1700aa95e7190439', False, 
"""x.__setslice__(i, j, y) <==> x[i:j]=y

Use  of negative indices is not supported."""),

],


'list.__sizeof__': [
('de31bd9285e82f906e64f2421e3ac1d2', False, 
"""L.__sizeof__() -- size of L in memory, in bytes"""),

],


'list.append': [
('74e1f1b2b208d21368889ace93f77973', False, 
"""L.append(object) -- append object to end"""),

],


'list.count': [
('a8ece113894bbbc3356303a9db74974b', False, 
"""L.count(value) -> integer -- return number of occurrences of value"""),

],


'list.extend': [
('e60f787d6ee0cc6b3df6720b120cb352', False, 
"""L.extend(iterable) -- extend list by appending elements from the iterable"""),

],


'list.index': [
('6c83bf00f2cb7e587b3c1b1557ff0fd1', False, 
"""L.index(value, [start, [stop]]) -> integer -- return first index of value.
Raises ValueError if the value is not present."""),

],


'list.insert': [
('57248faab9bd8d582a362bc6cf0df0f4', False, 
"""L.insert(index, object) -- index の直前にオブジェクトを挿入します"""),

],


'list.pop': [
('304c38ee14ef43586dd7a2f6adb555f9', False, 
"""L.pop([index]) -> item -- remove and return item at index (default last).
Raises IndexError if list is empty or index is out of range."""),

],


'list.remove': [
('9afc20fb675acd27bc32b8c3da85fabb', False, 
"""L.remove(value) -- remove first occurrence of value.
Raises ValueError if the value is not present."""),

],


'list.reverse': [
('8ccfcbea80039edb7ad8c103ee4d9a4b', False, 
"""L.reverse() -- reverse *IN PLACE*"""),

],


'list.sort': [
('06af010a2edc539d82eeda79e0cf8a66', True, 
"""L.sort(cmp=None, key=None, reverse=False) -- *インプレースの* ソート;
cmp(x, y) -> -1, 0, 1"""),

],


'locals': [
('4856bfbdf8cc61510a282523b7b943ee', False, 
"""locals() -> dictionary

Update and return a dictionary containing the current scope\'s local variables."""),

],


'long': [
('fce09844a7b4dac492d52f4de5d891bb', False, 
"""long(x[, base]) -> integer

Convert a string or number to a long integer, if possible.  A floating
point argument will be truncated towards zero (this does not include a
string representation of a floating point number!)  When converting a
string, use the optional base.  It is an error to supply a base when
converting a non-string."""),

],


'long.__abs__': [
('f2abd704a5f550221ed980b2e2705c32', False, 
"""x.__abs__() <==> abs(x)"""),

],


'long.__add__': [
('e6460aedb37b9d9bab7a60fb4f7dbaa6', False, 
"""x.__add__(y) <==> x+y"""),

],


'long.__and__': [
('34f22603582785806906d3a619fbff20', False, 
"""x.__and__(y) <==> x&y"""),

],


'long.__coerce__': [
('3d0dc814e0e5f1542dfcb94e85548628', False, 
"""x.__coerce__(y) <==> coerce(x, y)"""),

],


'long.__div__': [
('4c99c4ef649797ccba5eac04ff19ddb2', False, 
"""x.__div__(y) <==> x/y"""),

],


'long.__divmod__': [
('2b7d2620e0eea6f731d872ecd08e9db0', False, 
"""x.__divmod__(y) <==> divmod(x, y)"""),

],


'long.__float__': [
('4fda8084fbf981f8ca05d3269cac8fff', False, 
"""x.__float__() <==> float(x)"""),

],


'long.__floordiv__': [
('9a95fb992e47a548c67dd066dc18db92', False, 
"""x.__floordiv__(y) <==> x//y"""),

],


'long.__format__': [
('d41d8cd98f00b204e9800998ecf8427e', False, 
""""""),

],


'long.__getnewargs__': [
('d41d8cd98f00b204e9800998ecf8427e', False, 
""""""),

],


'long.__hex__': [
('90d697452be414d8975c8d8c6f7a2555', False, 
"""x.__hex__() <==> hex(x)"""),

],


'long.__index__': [
('41003bb787667a27a886984ca53d92e4', False, 
"""x[y:z] <==> x[y.__index__():z.__index__()]"""),

],


'long.__int__': [
('4ce28b4400b621494ac706c935c68a5c', False, 
"""x.__int__() <==> int(x)"""),

],


'long.__invert__': [
('fe2ef705f0edf495578f68b26139508a', False, 
"""x.__invert__() <==> ~x"""),

],


'long.__long__': [
('8c929f31b1228256035450345e93d7c8', False, 
"""x.__long__() <==> long(x)"""),

],


'long.__lshift__': [
('caddc2d6a334913487a8ae40dde8f2ba', False, 
"""x.__lshift__(y) <==> x<<y"""),

],


'long.__mod__': [
('6833114697ac82c60289fa24897eabf0', False, 
"""x.__mod__(y) <==> x%y"""),

],


'long.__mul__': [
('131e3ee8270a7e3a4eb3048963c3035f', False, 
"""x.__mul__(y) <==> x*y"""),

],


'long.__neg__': [
('b8116e2ccb4eb620a227d47d5ade8aab', False, 
"""x.__neg__() <==> -x"""),

],


'long.__nonzero__': [
('6ef831e34b2bd8389823930cdc5da741', False, 
"""x.__nonzero__() <==> x != 0"""),

],


'long.__oct__': [
('665bf5f8194659353210e20cbcb48754', False, 
"""x.__oct__() <==> oct(x)"""),

],


'long.__or__': [
('5aaa9cc7414a761ca43f7b6098059d20', False, 
"""x.__or__(y) <==> x|y"""),

],


'long.__pos__': [
('a918e20eebd49d8da08d2c4fd79d3c2e', False, 
"""x.__pos__() <==> +x"""),

],


'long.__pow__': [
('cf0ec3f8787ff00d59011db965541daf', False, 
"""x.__pow__(y[, z]) <==> pow(x, y[, z])"""),

],


'long.__radd__': [
('b25ae2b25d815baf4bd20478a2a0f5fa', False, 
"""x.__radd__(y) <==> y+x"""),

],


'long.__rand__': [
('4e31b1b862f6ec29e32800270e841ea4', False, 
"""x.__rand__(y) <==> y&x"""),

],


'long.__rdiv__': [
('cbbf46f634bdd2cf96890cdd6f6e8818', False, 
"""x.__rdiv__(y) <==> y/x"""),

],


'long.__rdivmod__': [
('e0f8f012671ac842a6e3b5c1b626c425', False, 
"""x.__rdivmod__(y) <==> divmod(y, x)"""),

],


'long.__rfloordiv__': [
('65d54e9fd86aeeaf263c3295725f8779', False, 
"""x.__rfloordiv__(y) <==> y//x"""),

],


'long.__rlshift__': [
('f6da8b5ae2cf6302760201a17cae0f59', False, 
"""x.__rlshift__(y) <==> y<<x"""),

],


'long.__rmod__': [
('06f1130e0513ae2be0f9c61a70a181a4', False, 
"""x.__rmod__(y) <==> y%x"""),

],


'long.__rmul__': [
('6ee329cd333c8616bca5d4eec3709a6d', False, 
"""x.__rmul__(y) <==> y*x"""),

],


'long.__ror__': [
('da4d0348ca64c8c3d0aced68631472e6', False, 
"""x.__ror__(y) <==> y|x"""),

],


'long.__rpow__': [
('bcab33856c7f1ac53d2945d8680042a0', False, 
"""y.__rpow__(x[, z]) <==> pow(x, y[, z])"""),

],


'long.__rrshift__': [
('1086736a2257659a74d27eb32075a046', False, 
"""x.__rrshift__(y) <==> y>>x"""),

],


'long.__rshift__': [
('4747cfab9ec34d9f8bf93576a3c56410', False, 
"""x.__rshift__(y) <==> x>>y"""),

],


'long.__rsub__': [
('38c09ada0390bc15efda2fda66cf5bf0', False, 
"""x.__rsub__(y) <==> y-x"""),

],


'long.__rtruediv__': [
('d27e2573016197cc6beff9a155d1a605', False, 
"""x.__rtruediv__(y) <==> y/x"""),

],


'long.__rxor__': [
('70015a9fed00e657f349025f83450c30', False, 
"""x.__rxor__(y) <==> y^x"""),

],


'long.__sizeof__': [
('ddaece5f656d3fcfb42aba2a721e5567', False, 
"""Returns size in memory, in bytes"""),

],


'long.__sub__': [
('f311f7fcb90645e03097a51bf2c3ae3b', False, 
"""x.__sub__(y) <==> x-y"""),

],


'long.__truediv__': [
('a3b7c4cb9a3324a0fef052ee4d9d94aa', False, 
"""x.__truediv__(y) <==> x/y"""),

],


'long.__trunc__': [
('5f7705c348f8ea982f2cc17fa738baf3', False, 
"""Truncating an Integral returns itself."""),

],


'long.__xor__': [
('6c6511aa3cefcc142940d3d29d9fc4dd', False, 
"""x.__xor__(y) <==> x^y"""),

],


'long.conjugate': [
('59e05b01284295ac6a228e99972d688c', False, 
"""Returns self, the complex conjugate of any long."""),

],


'long.denominator': [
('58dade7e0e5478df7f26c0765e432ac2', False, 
"""the denominator of a rational number in lowest terms"""),

],


'long.imag': [
('d213520f337cea7606f1f1c12f1dc6b5', False, 
"""the imaginary part of a complex number"""),

],


'long.numerator': [
('f508b9e2647828fea347ac4759c7aaca', False, 
"""the numerator of a rational number in lowest terms"""),

],


'long.real': [
('72d30dc49502e1a2aa13e8eaa71c378e', False, 
"""the real part of a complex number"""),

],


'map': [
('4f1d6dc20a89b4dfcefba7ea3b65a015', False, 
"""map(function, sequence[, sequence, ...]) -> list

Return a list of the results of applying the function to the items of
the argument sequence(s).  If more than one sequence is given, the
function is called with an argument list consisting of the corresponding
item of each sequence, substituting None for missing values when not all
sequences have the same length.  If the function is None, return a list of
the items of the sequence (or a list of tuples if more than one sequence)."""),

],


'max': [
('a6b26de32f7e5233cd21956319a75e4c', False, 
"""max(iterable[, key=func]) -> value
max(a, b, c, ...[, key=func]) -> value

With a single iterable argument, return its largest item.
With two or more arguments, return the largest argument."""),

],


'min': [
('41ad3ac377ad5dbcb1c39d7eab64211b', False, 
"""min(iterable[, key=func]) -> value
min(a, b, c, ...[, key=func]) -> value

With a single iterable argument, return its smallest item.
With two or more arguments, return the smallest argument."""),

],


'next': [
('d3dd2ae9296fe0c886bcf3c1cc73ca2d', False, 
"""next(iterator[, default])

Return the next item from the iterator. If default is given and the iterator
is exhausted, it is returned instead of raising StopIteration."""),

],


'object': [
('622b06454f7fae478797bb48c8f6b51e', False, 
"""The most base type"""),

],


'object.__base__': [
('d41d8cd98f00b204e9800998ecf8427e', False, 
""""""),

],


'object.__call__': [
('2859cbed6fd98f9e1100536685b788eb', False, 
"""x.__call__(...) <==> x(...)"""),

],


'object.__cmp__': [
('9a1d06e96409107238d95a6daeb87aeb', False, 
"""x.__cmp__(y) <==> cmp(x,y)"""),

],


'object.__delattr__': [
('baa3cf4c149b70a2869173e9a5ced6df', False, 
"""x.__delattr__(\'name\') <==> del x.name"""),

],


'object.__dict__': [
('d41d8cd98f00b204e9800998ecf8427e', False, 
""""""),

],


'object.__eq__': [
('29276e56c1f9b89c0e4975783c563226', False, 
"""x.__eq__(y) <==> x==y"""),

],


'object.__ge__': [
('a40b7fe72a380879d7602be9b639db1b', False, 
"""x.__ge__(y) <==> x>=y"""),

],


'object.__getattribute__': [
('efa80438e88a77b4eba07ebe2d9ceb85', False, 
"""x.__getattribute__(\'name\') <==> x.name"""),

],


'object.__gt__': [
('43f3c9de3ba1d0a78dea8d37b57bff37', False, 
"""x.__gt__(y) <==> x>y"""),

],


'object.__hash__': [
('63a96d56ab20e8afcaf282823c66d409', False, 
"""x.__hash__() <==> hash(x)"""),

],


'object.__init__': [
('dfd263e1aebbb882dd7ff3335c71c9d6', False, 
"""x.__init__(...) initializes x; see x.__class__.__doc__ for signature"""),

],


'object.__instancecheck__': [
('d41d8cd98f00b204e9800998ecf8427e', False, 
""""""),

],


'object.__le__': [
('486eb7462a194cfb7ba27a685d3c6ec3', False, 
"""x.__le__(y) <==> x<=y"""),

],


'object.__lt__': [
('803809016499ca6afb70031b8fc55efe', False, 
"""x.__lt__(y) <==> x<y"""),

],


'object.__ne__': [
('1ffca5c8e0f2a871a1986db525d30469', False, 
"""x.__ne__(y) <==> x!=y"""),

],


'object.__repr__': [
('d7ecf995070b7d400aad745f917dd8f8', False, 
"""x.__repr__() <==> repr(x)"""),

],


'object.__setattr__': [
('464e7714ff75315810a899988772b5eb', False, 
"""x.__setattr__(\'name\', value) <==> x.name = value"""),

],


'object.__str__': [
('5f53e31d167624726f84cafe0dfc5af2', False, 
"""x.__str__() <==> str(x)"""),

],


'object.__subclasscheck__': [
('d41d8cd98f00b204e9800998ecf8427e', False, 
""""""),

],


'object.__subclasses__': [
('3040d8c0c99db512728d4becd924ba50', False, 
"""__subclasses__() -> list of immediate subclasses"""),

],


'object.mro': [
('abee960fd4c96e5f077d72e596fd743e', False, 
"""mro() -> list
return a type\'s method resolution order"""),

],


'oct': [
('2ffdf217696bbe7097c6ce7f3a5e1914', False, 
"""oct(number) -> string

Return the octal representation of an integer or long integer."""),

],


'open': [
('2b0a37bf7fa5053760e5679bcaa64ca4', False, 
"""open(name[, mode[, buffering]]) -> file object

Open a file using the file() type, returns a file object.  This is the
preferred way to open a file."""),

],


'ord': [
('5182e6eb639bc6f37a880f517f6fdf49', False, 
"""ord(c) -> integer

Return the integer ordinal of a one-character string."""),

],


'pow': [
('46375481410b2c68d438af3ca428179b', False, 
"""pow(x, y[, z]) -> number

With two arguments, equivalent to x**y.  With three arguments,
equivalent to (x**y) % z, but may be more efficient (e.g. for longs)."""),

],


'print': [
('e88b4d1968277cf3526e038ba33d2631', False, 
"""print(value, ..., sep=\' \', end=\'
\', file=sys.stdout)

Prints the values to a stream, or to sys.stdout by default.
Optional keyword arguments:
file: a file-like object (stream); defaults to the current sys.stdout.
sep:  string inserted between values, default a space.
end:  string appended after the last value, default a newline."""),

],


'property': [
('9ab9f768d201246f8c1e292682f2bc8a', False, 
"""property(fget=None, fset=None, fdel=None, doc=None) -> property attribute

fget is a function to be used for getting an attribute value, and likewise
fset is a function for setting, and fdel a function for del\'ing, an
attribute.  Typical use is to define a managed attribute x:
class C(object):
    def getx(self): return self._x
    def setx(self, value): self._x = value
    def delx(self): del self._x
    x = property(getx, setx, delx, \"I\'m the \'x\' property.\")

Decorators make defining new properties or modifying existing ones easy:
class C(object):
    @property
    def x(self): return self._x
    @x.setter
    def x(self, value): self._x = value
    @x.deleter
    def x(self): del self._x"""),

],


'property.__delete__': [
('b1d1c2c29133b2563f3636942de4e9f7', False, 
"""descr.__delete__(obj)"""),

],


'property.__get__': [
('d26800418397c66c49e33dcfd65f7f03', False, 
"""descr.__get__(obj[, type]) -> value"""),

],


'property.__set__': [
('992f2bc40ed7f813eec897f223778c1c', False, 
"""descr.__set__(obj, value)"""),

],


'property.deleter': [
('fcbb00fc989df13ba99f395077ba5e57', False, 
"""Descriptor to change the deleter on a property."""),

],


'property.fdel': [
('d41d8cd98f00b204e9800998ecf8427e', False, 
""""""),

],


'property.fget': [
('d41d8cd98f00b204e9800998ecf8427e', False, 
""""""),

],


'property.fset': [
('d41d8cd98f00b204e9800998ecf8427e', False, 
""""""),

],


'property.getter': [
('5a8f183b40bde15a3ec6f52230ce321e', False, 
"""Descriptor to change the getter on a property."""),

],


'property.setter': [
('bf9c04fef6efeeebf31c2030ffac8e0e', False, 
"""Descriptor to change the setter on a property."""),

],


'range': [
('7bb9e20f3cc06b8c278c9e3d382b40dd', False, 
"""range([start,] stop[, step]) -> list of integers

Return a list containing an arithmetic progression of integers.
range(i, j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults to 0.
When step is given, it specifies the increment (or decrement).
For example, range(4) returns [0, 1, 2, 3].  The end point is omitted!
These are exactly the valid indices for a list of 4 elements."""),

],


'raw_input': [
('eaa6afba1062a23e52693be69bb692e0', False, 
"""raw_input([prompt]) -> string

Read a string from standard input.  The trailing newline is stripped.
If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
On Unix, GNU readline is used if enabled.  The prompt string, if given,
is printed without a trailing newline before reading."""),

],


'reduce': [
('6296f59949fee3e92d5a8cd1db9f88af', False, 
"""reduce(function, sequence[, initial]) -> value

Apply a function of two arguments cumulatively to the items of a sequence,
from left to right, so as to reduce the sequence to a single value.
For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
of the sequence in the calculation, and serves as a default when the
sequence is empty."""),

],


'reload': [
('8f7dfb0922c69b3f397e59b61faebc94', False, 
"""reload(module) -> module

Reload the module.  The module must have been successfully imported before."""),

],


'repr': [
('468439fa51e9b701373d8d882f9097a1', False, 
"""repr(object) -> string

Return the canonical string representation of the object.
For most object types, eval(repr(object)) == object."""),

],


'reversed': [
('794b3b47c428068357ebe55c5fe28410', False, 
"""reversed(sequence) -> reverse iterator over values of the sequence

Return a reverse iterator"""),

],


'reversed.__iter__': [
('448f3e7033f2161670d1a383ba662d22', False, 
"""x.__iter__() <==> iter(x)"""),

],


'reversed.__length_hint__': [
('b2cce6cd693af2796114f5da3bdf4b13', False, 
"""len(list(it)) の推定値を返すプライベートメソッドです。"""),

],


'reversed.next': [
('288fd681cdf3b0a8149971d514e6e91e', True, 
"""x.next() -> 次の値か、 StopIteration"""),

],


'round': [
('19a627ec259be66c9f63d1584f0eb2dd', False, 
"""round(number[, ndigits]) -> floating point number

Round a number to a given precision in decimal digits (default 0 digits).
This always returns a floating point number.  Precision may be negative."""),

],


'set': [
('42ce741f5cf5364771474fbdbd940054', False, 
"""set(iterable) --> set object

Build an unordered collection of unique elements."""),

],


'set.__and__': [
('34f22603582785806906d3a619fbff20', False, 
"""x.__and__(y) <==> x&y"""),

],


'set.__contains__': [
('ffd9e4fc21822f7b05e9a9147e7ab5cb', False, 
"""x.__contains__(y) <==> y in x."""),

],


'set.__iand__': [
('cf858aaa63286dedf0e14bef2167c873', False, 
"""x.__iand__(y) <==> x&y"""),

],


'set.__ior__': [
('346f7c5df93643b7548b68394024a7b9', False, 
"""x.__ior__(y) <==> x|y"""),

],


'set.__isub__': [
('ba6d4e15c4a6cc79bcf86dd74304b688', False, 
"""x.__isub__(y) <==> x-y"""),

],


'set.__iter__': [
('448f3e7033f2161670d1a383ba662d22', False, 
"""x.__iter__() <==> iter(x)"""),

],


'set.__ixor__': [
('6eb535bd792708eab3419559f724dd1c', False, 
"""x.__ixor__(y) <==> x^y"""),

],


'set.__len__': [
('3d6e075527d9b8e03b83a311002c24c1', False, 
"""x.__len__() <==> len(x)"""),

],


'set.__or__': [
('5aaa9cc7414a761ca43f7b6098059d20', False, 
"""x.__or__(y) <==> x|y"""),

],


'set.__rand__': [
('4e31b1b862f6ec29e32800270e841ea4', False, 
"""x.__rand__(y) <==> y&x"""),

],


'set.__reduce__': [
('588c3883072aa7e007926eb32098cdfc', False, 
"""Return state information for pickling."""),

],


'set.__ror__': [
('da4d0348ca64c8c3d0aced68631472e6', False, 
"""x.__ror__(y) <==> y|x"""),

],


'set.__rsub__': [
('38c09ada0390bc15efda2fda66cf5bf0', False, 
"""x.__rsub__(y) <==> y-x"""),

],


'set.__rxor__': [
('70015a9fed00e657f349025f83450c30', False, 
"""x.__rxor__(y) <==> y^x"""),

],


'set.__sizeof__': [
('e2b18bc0b4abb612dc21e3efe830695b', False, 
"""S.__sizeof__() -> size of S in memory, in bytes"""),

],


'set.__sub__': [
('f311f7fcb90645e03097a51bf2c3ae3b', False, 
"""x.__sub__(y) <==> x-y"""),

],


'set.__xor__': [
('6c6511aa3cefcc142940d3d29d9fc4dd', False, 
"""x.__xor__(y) <==> x^y"""),

],


'set.add': [
('60d7e124029bc4b2f913a1f0e6b52e1f', False, 
"""Add an element to a set.

This has no effect if the element is already present."""),

],


'set.clear': [
('4ed1ef7fb4c60bed6c9226e16fc1765f', False, 
"""Remove all elements from this set."""),

],


'set.copy': [
('42a24c7d25e5a9cfeeb1414761b60e42', False, 
"""Return a shallow copy of a set."""),

],


'set.difference': [
('33b586d58256cd0addd07d52a35c3248', False, 
"""Return the difference of two or more sets as a new set.

(i.e. all elements that are in this set but not the others.)"""),

],


'set.difference_update': [
('3c0bbbbb158a31113ac32382f5a9519e', False, 
"""Remove all elements of another set from this set."""),

],


'set.discard': [
('c5ef0b46986c54a6e8d4b6678ed7d032', False, 
"""Remove an element from a set if it is a member.

If the element is not a member, do nothing."""),

],


'set.intersection': [
('2fb7b3bddc0bd6ec5ecba2d509250429', False, 
"""Return the intersection of two sets as a new set.

(i.e. all elements that are in both sets.)"""),

],


'set.intersection_update': [
('fbe895398c951e4802bb37aa8012ceec', False, 
"""Update a set with the intersection of itself and another."""),

],


'set.isdisjoint': [
('a4982a4d169a3b3f6a46cd0f44c79bc7', False, 
"""Return True if two sets have a null intersection."""),

],


'set.issubset': [
('88902362cc72f0758c8a79935b7d993c', False, 
"""Report whether another set contains this set."""),

],


'set.issuperset': [
('5598fc98f1739ce2f114650df98889dd', False, 
"""Report whether this set contains another set."""),

],


'set.pop': [
('2ff73210c0c7a246d368518b879824e5', False, 
"""Remove and return an arbitrary set element.
Raises KeyError if the set is empty."""),

],


'set.remove': [
('bd0d8a7c4e85faf2666e8ce9fabbed7c', False, 
"""Remove an element from a set; it must be a member.

If the element is not a member, raise a KeyError."""),

],


'set.symmetric_difference': [
('9fd3f2e18bffee87b7a970d97beb5b0d', False, 
"""Return the symmetric difference of two sets as a new set.

(i.e. all elements that are in exactly one of the sets.)"""),

],


'set.symmetric_difference_update': [
('d4728c390c5861cf1ce398082a0c3466', False, 
"""Update a set with the symmetric difference of itself and another."""),

],


'set.union': [
('9a8f2a81d7820cbddf66d9b1c1f909ae', False, 
"""Return the union of sets as a new set.

(i.e. all elements that are in either set.)"""),

],


'set.update': [
('1f6e45e95fc169082d4bdc0d055c29a0', False, 
"""Update a set with the union of itself and others."""),

],


'setattr': [
('fab8123634bb086cc20c45269823d2aa', False, 
"""setattr(object, name, value)

Set a named attribute on an object; setattr(x, \'y\', v) is equivalent to
``x.y = v\'\'."""),

],


'slice': [
('addd0c737861bece1f69887b0e01094b', False, 
"""slice([start,] stop[, step])

Create a slice object.  This is used for extended slicing (e.g. a[0:10:2])."""),

],


'slice.__reduce__': [
('588c3883072aa7e007926eb32098cdfc', False, 
"""Return state information for pickling."""),

],


'slice.indices': [
('ba66026b5918e567fbe3047e00fbb222', False, 
"""S.indices(len) -> (start, stop, stride)

Assuming a sequence of length len, calculate the start and stop
indices, and the stride length of the extended slice described by
S. Out of bounds indices are clipped in a manner consistent with the
handling of normal slices."""),

],


'slice.start': [
('d41d8cd98f00b204e9800998ecf8427e', False, 
""""""),

],


'slice.step': [
('d41d8cd98f00b204e9800998ecf8427e', False, 
""""""),

],


'slice.stop': [
('d41d8cd98f00b204e9800998ecf8427e', False, 
""""""),

],


'sorted': [
('1678eee8a1a4933421a3c53c06680519', False, 
"""sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list"""),

],


'staticmethod': [
('433a695a4a61536645ea30aaafec0577', False, 
"""staticmethod(function) -> method

Convert a function to be a static method.

A static method does not receive an implicit first argument.
To declare a static method, use this idiom:

     class C:
         def f(arg1, arg2, ...): ...
         f = staticmethod(f)

It can be called either on the class (e.g. C.f()) or on an instance
(e.g. C().f()).  The instance is ignored except for its class.

Static methods in Python are similar to those found in Java or C++.
For a more advanced concept, see the classmethod builtin."""),

],


'staticmethod.__get__': [
('d26800418397c66c49e33dcfd65f7f03', False, 
"""descr.__get__(obj[, type]) -> value"""),

],


'str': [
('08784c92552a95871cd678714cb3fec9', False, 
"""str(object) -> string

Return a nice string representation of the object.
If the argument is a string, the return value is the same object."""),

],


'str.__add__': [
('e6460aedb37b9d9bab7a60fb4f7dbaa6', False, 
"""x.__add__(y) <==> x+y"""),

],


'str.__contains__': [
('3e4d608788a476ebb6efff2e2c3258bf', False, 
"""x.__contains__(y) <==> y in x"""),

],


'str.__format__': [
('82173bab563ead0a01ff9b3de7512b58', False, 
"""S.__format__(format_spec) -> unicode"""),

],


'str.__getitem__': [
('5b1a2fedeaae4789f80b680bc5ab6529', False, 
"""x.__getitem__(y) <==> x[y]"""),

],


'str.__getnewargs__': [
('d41d8cd98f00b204e9800998ecf8427e', False, 
""""""),

],


'str.__getslice__': [
('d8dc8374f2dd864544396f2f0b4f7f25', True, 
"""x.__getslice__(i, j) <==> x[i:j]

負のインデクス値は指定できません。"""),

],


'str.__len__': [
('3d6e075527d9b8e03b83a311002c24c1', False, 
"""x.__len__() <==> len(x)"""),

],


'str.__mod__': [
('6833114697ac82c60289fa24897eabf0', False, 
"""x.__mod__(y) <==> x%y"""),

],


'str.__mul__': [
('81afa97dd875518810269060ffb7d938', False, 
"""x.__mul__(n) <==> x*n"""),

],


'str.__rmod__': [
('06f1130e0513ae2be0f9c61a70a181a4', False, 
"""x.__rmod__(y) <==> y%x"""),

],


'str.__rmul__': [
('3705f779f36813dd93b82ce068898521', False, 
"""x.__rmul__(n) <==> n*x"""),

],


'str.__sizeof__': [
('e2b18bc0b4abb612dc21e3efe830695b', False, 
"""S.__sizeof__() -> size of S in memory, in bytes"""),

],


'str.capitalize': [
('f578921f3ce24dd86a09fb9cbd647848', False, 
"""S.capitalize() -> string

Return a copy of the string S with only its first character
capitalized."""),

],


'str.center': [
('2abac179699a29ce7e4690dcee3b2cf8', False, 
"""S.center(width[, fillchar]) -> string

Return S centered in a string of length width. Padding is
done using the specified fill character (default is a space)"""),

],


'str.count': [
('bdfdea9d44d46755b3cb3a6d8ce528ce', False, 
"""S.count(sub[, start[, end]]) -> int

Return the number of non-overlapping occurrences of substring sub in
string S[start:end].  Optional arguments start and end are interpreted
as in slice notation."""),

],


'str.decode': [
('75172509c0ca93d261a8bef6979ad13d', False, 
"""S.decode([encoding[,errors]]) -> object

Decodes S using the codec registered for encoding. encoding defaults
to the default encoding. errors may be given to set a different error
handling scheme. Default is \'strict\' meaning that encoding errors raise
a UnicodeDecodeError. Other possible values are \'ignore\' and \'replace\'
as well as any other name registered with codecs.register_error that is
able to handle UnicodeDecodeErrors."""),

],


'str.encode': [
('bc4046a101b432e092a3db03db8a847f', False, 
"""S.encode([encoding[,errors]]) -> object

Encodes S using the codec registered for encoding. encoding defaults
to the default encoding. errors may be given to set a different error
handling scheme. Default is \'strict\' meaning that encoding errors raise
a UnicodeEncodeError. Other possible values are \'ignore\', \'replace\' and
\'xmlcharrefreplace\' as well as any other name registered with
codecs.register_error that is able to handle UnicodeEncodeErrors."""),

],


'str.endswith': [
('4a24e5dae45423aaab57f0238fc8950f', False, 
"""S.endswith(suffix[, start[, end]]) -> bool

Return True if S ends with the specified suffix, False otherwise.
With optional start, test S beginning at that position.
With optional end, stop comparing S at that position.
suffix can also be a tuple of strings to try."""),

],


'str.expandtabs': [
('931d6d822353ea129abcdbf228e7155a', False, 
"""S.expandtabs([tabsize]) -> string

Return a copy of S where all tab characters are expanded using spaces.
If tabsize is not given, a tab size of 8 characters is assumed."""),

],


'str.find': [
('8295b622ba64f5cce05f5873bed02a0b', False, 
"""S.find(sub [,start [,end]]) -> int

Return the lowest index in S where substring sub is found,
such that sub is contained within s[start:end].  Optional
arguments start and end are interpreted as in slice notation.

Return -1 on failure."""),

],


'str.format': [
('d4a96f14e23c814aeb32525becc4dc46', False, 
"""S.format(*args, **kwargs) -> unicode"""),

],


'str.index': [
('68f6202471bb734392d5a6515a6d31d9', False, 
"""S.index(sub [,start [,end]]) -> int

Like S.find() but raise ValueError when the substring is not found."""),

],


'str.isalnum': [
('13d96261e8e34d8aee847c122295615c', False, 
"""S.isalnum() -> bool

Return True if all characters in S are alphanumeric
and there is at least one character in S, False otherwise."""),

],


'str.isalpha': [
('8f4ade156adde577799680e6488f4504', False, 
"""S.isalpha() -> bool

Return True if all characters in S are alphabetic
and there is at least one character in S, False otherwise."""),

],


'str.isdigit': [
('91e2df8040313425a4dc8cf2de8d76b5', False, 
"""S.isdigit() -> bool

Return True if all characters in S are digits
and there is at least one character in S, False otherwise."""),

],


'str.islower': [
('eaa4bc5defa7637454abedbbc5ffe418', False, 
"""S.islower() -> bool

Return True if all cased characters in S are lowercase and there is
at least one cased character in S, False otherwise."""),

],


'str.isspace': [
('32499e932eb50049c9ba7bb483328f4a', False, 
"""S.isspace() -> bool

Return True if all characters in S are whitespace
and there is at least one character in S, False otherwise."""),

],


'str.istitle': [
('a19a7605bc623992cb08731b032c9be3', False, 
"""S.istitle() -> bool

Return True if S is a titlecased string and there is at least one
character in S, i.e. uppercase characters may only follow uncased
characters and lowercase characters only cased ones. Return False
otherwise."""),

],


'str.isupper': [
('dd332ce2b365599c597efce88489144d', False, 
"""S.isupper() -> bool

Return True if all cased characters in S are uppercase and there is
at least one cased character in S, False otherwise."""),

],


'str.join': [
('72978d5744a775e7fa271f9084711425', False, 
"""S.join(sequence) -> string

Return a string which is the concatenation of the strings in the
sequence.  The separator between elements is S."""),

],


'str.ljust': [
('99e330887fdee39083517c0cf927e523', False, 
"""S.ljust(width[, fillchar]) -> string

Return S left-justified in a string of length width. Padding is
done using the specified fill character (default is a space)."""),

],


'str.lower': [
('0014b70e12bdd7974339b07acf9487f1', False, 
"""S.lower() -> string

Return a copy of the string S converted to lowercase."""),

],


'str.lstrip': [
('ee9dacc199a189eb54ae57f0732365a4', False, 
"""S.lstrip([chars]) -> string or unicode

Return a copy of the string S with leading whitespace removed.
If chars is given and not None, remove characters in chars instead.
If chars is unicode, S will be converted to unicode before stripping"""),

],


'str.partition': [
('37c4ed512d00e3ae78a2bf82822a2f3a', True, 
"""S.partition(sep) -> (head, sep, tail)

S の中でセパレータ sep を探し、見つかった場合には、セパレータ以前
前の文字列、セパレータ本体、セパレータ以降の文字列からなる
タプルを返します。セパレータが見つからなかった場合には、 S と二つの
空文字列からなるタプルを返します。"""),

],


'str.replace': [
('91e33a5e3054cf2165a67a3d81274899', False, 
"""S.replace (old, new[, count]) -> string

Return a copy of string S with all occurrences of substring
old replaced by new.  If the optional argument count is
given, only the first count occurrences are replaced."""),

],


'str.rfind': [
('164c482da778d087533030f8b05c9312', False, 
"""S.rfind(sub [,start [,end]]) -> int

Return the highest index in S where substring sub is found,
such that sub is contained within s[start:end].  Optional
arguments start and end are interpreted as in slice notation.

Return -1 on failure."""),

],


'str.rindex': [
('692cfe4e689736506f26dcf813d08cb7', False, 
"""S.rindex(sub [,start [,end]]) -> int

Like S.rfind() but raise ValueError when the substring is not found."""),

],


'str.rjust': [
('04072f24aa81eb3214e21fa4ade5e410', False, 
"""S.rjust(width[, fillchar]) -> string

Return S right-justified in a string of length width. Padding is
done using the specified fill character (default is a space)"""),

],


'str.rpartition': [
('28d9d98510332ead6d76cf9dfff186bf', False, 
"""S.rpartition(sep) -> (tail, sep, head)

Search for the separator sep in S, starting at the end of S, and return
the part before it, the separator itself, and the part after it.  If the
separator is not found, return two empty strings and S."""),

],


'str.rsplit': [
('cb9db3d4761b50a616c7c1f527b0a15c', False, 
"""S.rsplit([sep [,maxsplit]]) -> list of strings

Return a list of the words in the string S, using sep as the
delimiter string, starting at the end of the string and working
to the front.  If maxsplit is given, at most maxsplit splits are
done. If sep is not specified or is None, any whitespace string
is a separator."""),

],


'str.rstrip': [
('ff544d56dc5865fb4b702cd344af4504', False, 
"""S.rstrip([chars]) -> string or unicode

Return a copy of the string S with trailing whitespace removed.
If chars is given and not None, remove characters in chars instead.
If chars is unicode, S will be converted to unicode before stripping"""),

],


'str.split': [
('4f066eba32c04bf5d1767ecab40ce7ab', False, 
"""S.split([sep [,maxsplit]]) -> list of strings

Return a list of the words in the string S, using sep as the
delimiter string.  If maxsplit is given, at most maxsplit
splits are done. If sep is not specified or is None, any
whitespace string is a separator and empty strings are removed
from the result."""),

],


'str.splitlines': [
('62bcd59857476bf056052d0418ae950e', False, 
"""S.splitlines([keepends]) -> list of strings

Return a list of the lines in S, breaking at line boundaries.
Line breaks are not included in the resulting list unless keepends
is given and true."""),

],


'str.startswith': [
('6a702388af225883f4b70108b98ac887', False, 
"""S.startswith(prefix[, start[, end]]) -> bool

Return True if S starts with the specified prefix, False otherwise.
With optional start, test S beginning at that position.
With optional end, stop comparing S at that position.
prefix can also be a tuple of strings to try."""),

],


'str.strip': [
('d527df0727b9a3db20c1875d4013d8a8', False, 
"""S.strip([chars]) -> string or unicode

Return a copy of the string S with leading and trailing
whitespace removed.
If chars is given and not None, remove characters in chars instead.
If chars is unicode, S will be converted to unicode before stripping"""),

],


'str.swapcase': [
('eb19da621355a5b1a88c2eb3d7f92001', False, 
"""S.swapcase() -> string

Return a copy of the string S with uppercase characters
converted to lowercase and vice versa."""),

],


'str.title': [
('52ac01e8a72a4a7fa4ead22b5aaeb6fc', False, 
"""S.title() -> string

Return a titlecased version of S, i.e. words start with uppercase
characters, all remaining cased characters have lowercase."""),

],


'str.translate': [
('549f25ac63c51932fceecddff857d389', False, 
"""S.translate(table [,deletechars]) -> string

Return a copy of the string S, where all characters occurring
in the optional argument deletechars are removed, and the
remaining characters have been mapped through the given
translation table, which must be a string of length 256."""),

],


'str.upper': [
('7a91d05ed33e1382ca2c9790f1000ba6', False, 
"""S.upper() -> string

Return a copy of the string S converted to uppercase."""),

],


'str.zfill': [
('afbf45ecee07349e7a6375bd0cd2f6c1', False, 
"""S.zfill(width) -> string

Pad a numeric string S with zeros on the left, to fill a field
of the specified width.  The string S is never truncated."""),

],


'sum': [
('8d878234789fc5c02399c793eb2e578b', False, 
"""sum(sequence[, start]) -> value

Returns the sum of a sequence of numbers (NOT strings) plus the value
of parameter \'start\' (which defaults to 0).  When the sequence is
empty, returns start."""),

],


'super': [
('cb690833ec6d46976aac99804626570c', False, 
"""super(type) -> unbound super object
super(type, obj) -> bound super object; requires isinstance(obj, type)
super(type, type2) -> bound super object; requires issubclass(type2, type)
Typical use to call a cooperative superclass method:
class C(B):
    def meth(self, arg):
         super(C, self).meth(arg)"""),

],


'super.__get__': [
('d26800418397c66c49e33dcfd65f7f03', False, 
"""descr.__get__(obj[, type]) -> value"""),

],


'super.__self__': [
('5f3ee8d208bd2a9e42d321371b4cb9bd', False, 
"""the instance invoking super(); may be None"""),

],


'super.__self_class__': [
('4c959cb7e694a396a6affbe00e3edc62', False, 
"""the type of the instance invoking super(); may be None"""),

],


'super.__thisclass__': [
('73320307b2feb9f2e0abc859028c8196', False, 
"""the class invoking super()"""),

],


'tuple': [
('71c643bbb90bf19a4636dfe6236f90ca', False, 
"""tuple() -> an empty tuple
tuple(sequence) -> tuple initialized from sequence\'s items

If the argument is a tuple, the return value is the same object."""),

],


'tuple.__add__': [
('e6460aedb37b9d9bab7a60fb4f7dbaa6', False, 
"""x.__add__(y) <==> x+y"""),

],


'tuple.__contains__': [
('3e4d608788a476ebb6efff2e2c3258bf', False, 
"""x.__contains__(y) <==> y in x"""),

],


'tuple.__getitem__': [
('5b1a2fedeaae4789f80b680bc5ab6529', False, 
"""x.__getitem__(y) <==> x[y]"""),

],


'tuple.__getnewargs__': [
('d41d8cd98f00b204e9800998ecf8427e', False, 
""""""),

],


'tuple.__getslice__': [
('d8dc8374f2dd864544396f2f0b4f7f25', False, 
"""x.__getslice__(i, j) <==> x[i:j]

Use of negative indices is not supported."""),

],


'tuple.__iter__': [
('448f3e7033f2161670d1a383ba662d22', False, 
"""x.__iter__() <==> iter(x)"""),

],


'tuple.__len__': [
('3d6e075527d9b8e03b83a311002c24c1', False, 
"""x.__len__() <==> len(x)"""),

],


'tuple.__mul__': [
('81afa97dd875518810269060ffb7d938', False, 
"""x.__mul__(n) <==> x*n"""),

],


'tuple.__rmul__': [
('3705f779f36813dd93b82ce068898521', False, 
"""x.__rmul__(n) <==> n*x"""),

],


'tuple.__sizeof__': [
('8d1569e07bea433700b3eb75b811e460', False, 
"""T.__sizeof__() -- size of T in memory, in bytes"""),

],


'tuple.count': [
('77d657da0a7b7181a46e8c1c92ea5eb8', False, 
"""T.count(value) -> integer -- return number of occurrences of value"""),

],


'tuple.index': [
('1f25244609a12938bf19b7a43276b285', False, 
"""T.index(value, [start, [stop]]) -> integer -- return first index of value.
Raises ValueError if the value is not present."""),

],


'type': [
('7ce047e7526201958f0575a41b2602fe', False, 
"""type(object) -> the object\'s type
type(name, bases, dict) -> a new type"""),

],


'type.__abstractmethods__': [
('d41d8cd98f00b204e9800998ecf8427e', False, 
""""""),

],


'type.__bases__': [
('d41d8cd98f00b204e9800998ecf8427e', False, 
""""""),

],


'type.__basicsize__': [
('d41d8cd98f00b204e9800998ecf8427e', False, 
""""""),

],


'type.__dictoffset__': [
('d41d8cd98f00b204e9800998ecf8427e', False, 
""""""),

],


'type.__flags__': [
('d41d8cd98f00b204e9800998ecf8427e', False, 
""""""),

],


'type.__itemsize__': [
('d41d8cd98f00b204e9800998ecf8427e', False, 
""""""),

],


'type.__mro__': [
('d41d8cd98f00b204e9800998ecf8427e', False, 
""""""),

],


'type.__weakrefoffset__': [
('d41d8cd98f00b204e9800998ecf8427e', False, 
""""""),

],


'unichr': [
('409a5211f707114fb8a3efff15cfd168', False, 
"""unichr(i) -> Unicode character

Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff."""),

],


'unicode': [
('72e1ad7314552303fd4d933305434529', False, 
"""unicode(string [, encoding[, errors]]) -> object

Create a new Unicode object from the given encoded string.
encoding defaults to the current default string encoding.
errors can be \'strict\', \'replace\' or \'ignore\' and defaults to \'strict\'."""),

],


'unicode.__add__': [
('e6460aedb37b9d9bab7a60fb4f7dbaa6', False, 
"""x.__add__(y) <==> x+y"""),

],


'unicode.__contains__': [
('3e4d608788a476ebb6efff2e2c3258bf', False, 
"""x.__contains__(y) <==> y in x"""),

],


'unicode.__format__': [
('82173bab563ead0a01ff9b3de7512b58', False, 
"""S.__format__(format_spec) -> unicode"""),

],


'unicode.__getitem__': [
('5b1a2fedeaae4789f80b680bc5ab6529', False, 
"""x.__getitem__(y) <==> x[y]"""),

],


'unicode.__getnewargs__': [
('d41d8cd98f00b204e9800998ecf8427e', False, 
""""""),

],


'unicode.__getslice__': [
('d8dc8374f2dd864544396f2f0b4f7f25', False, 
"""x.__getslice__(i, j) <==> x[i:j]

Use of negative indices is not supported."""),

],


'unicode.__len__': [
('3d6e075527d9b8e03b83a311002c24c1', False, 
"""x.__len__() <==> len(x)"""),

],


'unicode.__mod__': [
('6833114697ac82c60289fa24897eabf0', False, 
"""x.__mod__(y) <==> x%y"""),

],


'unicode.__mul__': [
('81afa97dd875518810269060ffb7d938', False, 
"""x.__mul__(n) <==> x*n"""),

],


'unicode.__rmod__': [
('06f1130e0513ae2be0f9c61a70a181a4', False, 
"""x.__rmod__(y) <==> y%x"""),

],


'unicode.__rmul__': [
('3705f779f36813dd93b82ce068898521', False, 
"""x.__rmul__(n) <==> n*x"""),

],


'unicode.__sizeof__': [
('e2b18bc0b4abb612dc21e3efe830695b', False, 
"""S.__sizeof__() -> size of S in memory, in bytes"""),

],


'unicode.capitalize': [
('4321cda1342e64ca24673eded27d57fb', False, 
"""S.capitalize() -> unicode

Return a capitalized version of S, i.e. make the first character
have upper case."""),

],


'unicode.center': [
('710f272530690748f4ddbceb0743d00c', False, 
"""S.center(width[, fillchar]) -> unicode

Return S centered in a Unicode string of length width. Padding is
done using the specified fill character (default is a space)"""),

],


'unicode.count': [
('7d873e6a9f3c597a4780faba9d75bc30', False, 
"""S.count(sub[, start[, end]]) -> int

Return the number of non-overlapping occurrences of substring sub in
Unicode string S[start:end].  Optional arguments start and end are
interpreted as in slice notation."""),

],


'unicode.decode': [
('dbf0d6767b65b6d955cfd266f7ea0de4', False, 
"""S.decode([encoding[,errors]]) -> string or unicode

Decodes S using the codec registered for encoding. encoding defaults
to the default encoding. errors may be given to set a different error
handling scheme. Default is \'strict\' meaning that encoding errors raise
a UnicodeDecodeError. Other possible values are \'ignore\' and \'replace\'
as well as any other name registerd with codecs.register_error that is
able to handle UnicodeDecodeErrors."""),

],


'unicode.encode': [
('68fd1a3dc3e4a8819fe56b494ca658db', False, 
"""S.encode([encoding[,errors]]) -> string or unicode

Encodes S using the codec registered for encoding. encoding defaults
to the default encoding. errors may be given to set a different error
handling scheme. Default is \'strict\' meaning that encoding errors raise
a UnicodeEncodeError. Other possible values are \'ignore\', \'replace\' and
\'xmlcharrefreplace\' as well as any other name registered with
codecs.register_error that can handle UnicodeEncodeErrors."""),

],


'unicode.endswith': [
('4a24e5dae45423aaab57f0238fc8950f', False, 
"""S.endswith(suffix[, start[, end]]) -> bool

Return True if S ends with the specified suffix, False otherwise.
With optional start, test S beginning at that position.
With optional end, stop comparing S at that position.
suffix can also be a tuple of strings to try."""),

],


'unicode.expandtabs': [
('738ebd67f885537d30b2504d14e9c414', True, 
"""S.expandtabs([tabsize]) -> unicode

S のコピーを生成し、S の中に含まれるすべてのタブ文字を複数のスペースに
変換して返します。 tabsize を指定しない場合、タブの幅を 8 スペースと
みなします。"""),

],


'unicode.find': [
('8295b622ba64f5cce05f5873bed02a0b', False, 
"""S.find(sub [,start [,end]]) -> int

Return the lowest index in S where substring sub is found,
such that sub is contained within s[start:end].  Optional
arguments start and end are interpreted as in slice notation.

Return -1 on failure."""),

],


'unicode.format': [
('d4a96f14e23c814aeb32525becc4dc46', False, 
"""S.format(*args, **kwargs) -> unicode"""),

],


'unicode.index': [
('68f6202471bb734392d5a6515a6d31d9', False, 
"""S.index(sub [,start [,end]]) -> int

Like S.find() but raise ValueError when the substring is not found."""),

],


'unicode.isalnum': [
('13d96261e8e34d8aee847c122295615c', False, 
"""S.isalnum() -> bool

Return True if all characters in S are alphanumeric
and there is at least one character in S, False otherwise."""),

],


'unicode.isalpha': [
('8f4ade156adde577799680e6488f4504', False, 
"""S.isalpha() -> bool

Return True if all characters in S are alphabetic
and there is at least one character in S, False otherwise."""),

],


'unicode.isdecimal': [
('2021d98ae7bfa115d400df742a63f81d', False, 
"""S.isdecimal() -> bool

Return True if there are only decimal characters in S,
False otherwise."""),

],


'unicode.isdigit': [
('91e2df8040313425a4dc8cf2de8d76b5', False, 
"""S.isdigit() -> bool

Return True if all characters in S are digits
and there is at least one character in S, False otherwise."""),

],


'unicode.islower': [
('eaa4bc5defa7637454abedbbc5ffe418', False, 
"""S.islower() -> bool

Return True if all cased characters in S are lowercase and there is
at least one cased character in S, False otherwise."""),

],


'unicode.isnumeric': [
('5e0203ff0869962c1fa8194e827d8d5f', False, 
"""S.isnumeric() -> bool

Return True if there are only numeric characters in S,
False otherwise."""),

],


'unicode.isspace': [
('32499e932eb50049c9ba7bb483328f4a', False, 
"""S.isspace() -> bool

Return True if all characters in S are whitespace
and there is at least one character in S, False otherwise."""),

],


'unicode.istitle': [
('cea646cab18b34e2e93d522c340c887d', False, 
"""S.istitle() -> bool

Return True if S is a titlecased string and there is at least one
character in S, i.e. upper- and titlecase characters may only
follow uncased characters and lowercase characters only cased ones.
Return False otherwise."""),

],


'unicode.isupper': [
('dd332ce2b365599c597efce88489144d', False, 
"""S.isupper() -> bool

Return True if all cased characters in S are uppercase and there is
at least one cased character in S, False otherwise."""),

],


'unicode.join': [
('bfaef17749cd64432a7d73dacdbecaad', False, 
"""S.join(sequence) -> unicode

Return a string which is the concatenation of the strings in the
sequence.  The separator between elements is S."""),

],


'unicode.ljust': [
('7ec03040c0ddf3b61fba2a15c9e2ebc8', False, 
"""S.ljust(width[, fillchar]) -> int

Return S left-justified in a Unicode string of length width. Padding is
done using the specified fill character (default is a space)."""),

],


'unicode.lower': [
('ecac4678c6e6d2f3877eeb87f8c65fea', False, 
"""S.lower() -> unicode

Return a copy of the string S converted to lowercase."""),

],


'unicode.lstrip': [
('b6ad63a1f9bb520066375f49c4750d12', True, 
"""S.lstrip([chars]) -> unicode

文字列 S から、先頭の空白文字を除去したコピーを返します。
引数 chars に None でない値を指定すると、空白文字の代わりに、
chars に含まれる文字を除去します。 chars が str 型の場合、
処理を行う前に chars を unicode 型に変換します。"""),

],


'unicode.partition': [
('37c4ed512d00e3ae78a2bf82822a2f3a', False, 
"""S.partition(sep) -> (head, sep, tail)

Search for the separator sep in S, and return the part before it,
the separator itself, and the part after it.  If the separator is not
found, return S and two empty strings."""),

],


'unicode.replace': [
('b15a3d262303ef065c4a86796c9f63a1', False, 
"""S.replace (old, new[, count]) -> unicode

Return a copy of S with all occurrences of substring
old replaced by new.  If the optional argument count is
given, only the first count occurrences are replaced."""),

],


'unicode.rfind': [
('164c482da778d087533030f8b05c9312', False, 
"""S.rfind(sub [,start [,end]]) -> int

Return the highest index in S where substring sub is found,
such that sub is contained within s[start:end].  Optional
arguments start and end are interpreted as in slice notation.

Return -1 on failure."""),

],


'unicode.rindex': [
('692cfe4e689736506f26dcf813d08cb7', False, 
"""S.rindex(sub [,start [,end]]) -> int

Like S.rfind() but raise ValueError when the substring is not found."""),

],


'unicode.rjust': [
('66e3e4bc67c2a76fc2b43a43801f5c99', False, 
"""S.rjust(width[, fillchar]) -> unicode

Return S right-justified in a Unicode string of length width. Padding is
done using the specified fill character (default is a space)."""),

],


'unicode.rpartition': [
('28d9d98510332ead6d76cf9dfff186bf', False, 
"""S.rpartition(sep) -> (tail, sep, head)

Search for the separator sep in S, starting at the end of S, and return
the part before it, the separator itself, and the part after it.  If the
separator is not found, return two empty strings and S."""),

],


'unicode.rsplit': [
('7bb28ac4e2899c34228a4bb676c5f81a', False, 
"""S.rsplit([sep [,maxsplit]]) -> list of strings

Return a list of the words in S, using sep as the
delimiter string, starting at the end of the string and
working to the front.  If maxsplit is given, at most maxsplit
splits are done. If sep is not specified, any whitespace string
is a separator."""),

],


'unicode.rstrip': [
('ab40aba9e3c6305bd74e3fd5f723c8c2', False, 
"""S.rstrip([chars]) -> unicode

Return a copy of the string S with trailing whitespace removed.
If chars is given and not None, remove characters in chars instead.
If chars is a str, it will be converted to unicode before stripping"""),

],


'unicode.split': [
('c1467e95e6d424d9af244d3987739f84', False, 
"""S.split([sep [,maxsplit]]) -> list of strings

Return a list of the words in S, using sep as the
delimiter string.  If maxsplit is given, at most maxsplit
splits are done. If sep is not specified or is None, any
whitespace string is a separator and empty strings are
removed from the result."""),

],


'unicode.splitlines': [
('5c944de466281f6e5f13b25392e26202', False, 
"""S.splitlines([keepends]]) -> list of strings

Return a list of the lines in S, breaking at line boundaries.
Line breaks are not included in the resulting list unless keepends
is given and true."""),

],


'unicode.startswith': [
('6a702388af225883f4b70108b98ac887', False, 
"""S.startswith(prefix[, start[, end]]) -> bool

Return True if S starts with the specified prefix, False otherwise.
With optional start, test S beginning at that position.
With optional end, stop comparing S at that position.
prefix can also be a tuple of strings to try."""),

],


'unicode.strip': [
('deb2df5f81c36895b182e3c3641b2c45', False, 
"""S.strip([chars]) -> unicode

Return a copy of the string S with leading and trailing
whitespace removed.
If chars is given and not None, remove characters in chars instead.
If chars is a str, it will be converted to unicode before stripping"""),

],


'unicode.swapcase': [
('a70e0cf4c5f96888f1e50eeea9fc499e', False, 
"""S.swapcase() -> unicode

Return a copy of S with uppercase characters converted to lowercase
and vice versa."""),

],


'unicode.title': [
('67baff67e70037fd3114ef65beb3668d', False, 
"""S.title() -> unicode

Return a titlecased version of S, i.e. words start with title case
characters, all remaining cased characters have lower case."""),

],


'unicode.translate': [
('cf69102cb588bfe7fc8e5538df1de316', False, 
"""S.translate(table) -> unicode

Return a copy of the string S, where all characters have been mapped
through the given translation table, which must be a mapping of
Unicode ordinals to Unicode ordinals, Unicode strings or None.
Unmapped characters are left untouched. Characters mapped to None
are deleted."""),

],


'unicode.upper': [
('f199ef7b403e28c5e02ecfb821e0c4b8', False, 
"""S.upper() -> unicode

Return a copy of S converted to uppercase."""),

],


'unicode.zfill': [
('135c700316939c205f6954e5a947cbe8', False, 
"""S.zfill(width) -> unicode

Pad a numeric string S with zeros on the left, to fill a field
of the specified width. The string S is never truncated."""),

],


'vars': [
('bf4bb7c124082ac64f7915d537535ce4', False, 
"""vars([object]) -> dictionary

Without arguments, equivalent to locals().
With an argument, equivalent to object.__dict__."""),

],


'xrange': [
('4ca83fb725c512d8f820a15771bae017', False, 
"""xrange([start,] stop[, step]) -> xrange object

Like range(), but instead of returning a list, returns an object that
generates the numbers in the range on demand.  For looping, this is 
slightly faster than range() and more memory efficient."""),

],


'xrange.__getitem__': [
('5b1a2fedeaae4789f80b680bc5ab6529', False, 
"""x.__getitem__(y) <==> x[y]"""),

],


'xrange.__iter__': [
('448f3e7033f2161670d1a383ba662d22', False, 
"""x.__iter__() <==> iter(x)"""),

],


'xrange.__len__': [
('3d6e075527d9b8e03b83a311002c24c1', False, 
"""x.__len__() <==> len(x)"""),

],


'xrange.__reduce__': [
('d41d8cd98f00b204e9800998ecf8427e', False, 
""""""),

],


'xrange.__reversed__': [
('6314bfd1914e790436822a6fd5b1cf97', False, 
"""Returns a reverse iterator."""),

],


'zip': [
('bd7b384e40b99992345ecc086d07422b', False, 
"""zip(seq1 [, seq2 [...]]) -> [(seq1[0], seq2[0] ...), (...)]

Return a list of tuples, where each tuple contains the i-th element
from each of the argument sequences.  The returned list is truncated
in length to the length of the shortest argument sequence."""),

],


}
