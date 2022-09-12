from os import path
import sys



from PySide2.QtCore import QRect,QCoreApplication,QMetaObject
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QWidget,QLabel,QGroupBox,QLineEdit,QPushButton,QComboBox,QVBoxLayout

fn="custom_genshin_launcher_v1.2"
fname=[f"{fn}.py",f"{fn}.exe",f"{fn}_t.exe"]
if path.basename(sys.argv[0]) not in fname:
    #import win32api, win32con
    from win32api import MessageBox
    from win32con import MB_ICONERROR
    MessageBox(0, "文件名称错误", "错误", MB_ICONERROR)
    exit()



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 761)
        MainWindow.setMouseTracking(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMouseTracking(True)
        self.win_con = QLabel(self.centralwidget)
        self.win_con.setObjectName(u"win_con")
        self.win_con.setGeometry(QRect(0, 0, 1281, 41))
        self.win_con.setMouseTracking(True)
        self.settings_group = QGroupBox(self.centralwidget)
        self.settings_group.setObjectName(u"settings_group")
        self.settings_group.setGeometry(QRect(240, 130, 801, 471))
        self.settings_group.setMouseTracking(True)
        self.settings = QLabel(self.settings_group)
        self.settings.setObjectName(u"settings")
        self.settings.setGeometry(QRect(0, 0, 241, 471))
        self.settings.setMouseTracking(True)
        self.setting_sel = QLabel(self.settings_group)
        self.setting_sel.setObjectName(u"setting_sel")
        self.setting_sel.setGeometry(QRect(240, 0, 561, 471))
        self.setting_sel.setMouseTracking(True)
        self.setting_exit = QLabel(self.settings_group)
        self.setting_exit.setObjectName(u"setting_exit")
        self.setting_exit.setGeometry(QRect(723, 30, 41, 41))
        self.setting_exit.setMouseTracking(True)
        self.settingsel_path = QLabel(self.settings_group)
        self.settingsel_path.setObjectName(u"settingsel_path")
        self.settingsel_path.setGeometry(QRect(0, 80, 241, 51))
        self.settingsel_path_bgp = QLabel(self.settings_group)
        self.settingsel_path_bgp.setObjectName(u"settingsel_path_bgp")
        self.settingsel_path_bgp.setGeometry(QRect(270, 60, 221, 51))
        self.settingsel_path_bgp_show = QLabel(self.settings_group)
        self.settingsel_path_bgp_show.setObjectName(u"settingsel_path_bgp_show")
        self.settingsel_path_bgp_show.setGeometry(QRect(270, 120, 381, 41))
        self.settingsel_path_bgp_selbt = QLabel(self.settings_group)
        self.settingsel_path_bgp_selbt.setObjectName(u"settingsel_path_bgp_selbt")
        self.settingsel_path_bgp_selbt.setGeometry(QRect(670, 120, 121, 41))
        font = QFont()
        font.setPointSize(15)
        self.settingsel_path_bgp_selbt.setFont(font)
        self.settingsel_path_bgp_selbt.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.settingsel_path_gl = QLabel(self.settings_group)
        self.settingsel_path_gl.setObjectName(u"settingsel_path_gl")
        self.settingsel_path_gl.setGeometry(QRect(270, 190, 221, 51))
        self.settingsel_path_gl_show = QLabel(self.settings_group)
        self.settingsel_path_gl_show.setObjectName(u"settingsel_path_gl_show")
        self.settingsel_path_gl_show.setGeometry(QRect(270, 250, 381, 41))
        self.settingsel_path_gl_selbt = QLabel(self.settings_group)
        self.settingsel_path_gl_selbt.setObjectName(u"settingsel_path_gl_selbt")
        self.settingsel_path_gl_selbt.setGeometry(QRect(670, 250, 121, 41))
        self.settingsel_path_gl_selbt.setFont(font)
        self.settingsel_path_gl_selbt.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.settingsel_path_gs = QLabel(self.settings_group)
        self.settingsel_path_gs.setObjectName(u"settingsel_path_gs")
        self.settingsel_path_gs.setGeometry(QRect(270, 320, 221, 51))
        self.settingsel_path_gs_show = QLabel(self.settings_group)
        self.settingsel_path_gs_show.setObjectName(u"settingsel_path_gs_show")
        self.settingsel_path_gs_show.setGeometry(QRect(270, 380, 381, 41))
        self.settingsel_path_gs_selbt = QLabel(self.settings_group)
        self.settingsel_path_gs_selbt.setObjectName(u"settingsel_path_gs_selbt")
        self.settingsel_path_gs_selbt.setGeometry(QRect(670, 380, 121, 41))
        self.settingsel_path_gs_selbt.setFont(font)
        self.settingsel_path_gs_selbt.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.settingsel_change2i = QLabel(self.settings_group)
        self.settingsel_change2i.setObjectName(u"settingsel_change2i")
        self.settingsel_change2i.setGeometry(QRect(0, 140, 241, 51))
        self.settingsel_change2i_zip = QLabel(self.settings_group)
        self.settingsel_change2i_zip.setObjectName(u"settingsel_change2i_zip")
        self.settingsel_change2i_zip.setGeometry(QRect(270, 61, 221, 51))
        self.settingsel_change2i_zip_show = QLabel(self.settings_group)
        self.settingsel_change2i_zip_show.setObjectName(u"settingsel_change2i_zip_show")
        self.settingsel_change2i_zip_show.setGeometry(QRect(270, 120, 221, 51))
        font1 = QFont()
        font1.setPointSize(20)
        self.settingsel_change2i_zip_show.setFont(font1)
        self.settingsel_change2i_zip_show.setAlignment(Qt.AlignCenter)
        self.settingsel_change2i_zip_selbt = QLabel(self.settings_group)
        self.settingsel_change2i_zip_selbt.setObjectName(u"settingsel_change2i_zip_selbt")
        self.settingsel_change2i_zip_selbt.setGeometry(QRect(530, 130, 121, 41))
        self.settingsel_change2i_zip_selbt.setFont(font)
        self.settingsel_change2i_zip_selbt.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.settingsel_change2i_selbt = QLabel(self.settings_group)
        self.settingsel_change2i_selbt.setObjectName(u"settingsel_change2i_selbt")
        self.settingsel_change2i_selbt.setGeometry(QRect(370, 220, 121, 41))
        self.settingsel_change2i_selbt.setFont(font)
        self.settingsel_change2i_selbt.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.settingsel_change2i_download = QLabel(self.settings_group)
        self.settingsel_change2i_download.setObjectName(u"settingsel_change2i_download")
        self.settingsel_change2i_download.setGeometry(QRect(600, 420, 181, 31))
        self.settingsel_change2i_download.setFont(font)
        self.settingsel_change2i_download.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.settingsel_change2i_article = QLabel(self.settings_group)
        self.settingsel_change2i_article.setObjectName(u"settingsel_change2i_article")
        self.settingsel_change2i_article.setGeometry(QRect(600, 390, 181, 31))
        self.settingsel_change2i_article.setFont(font)
        self.settingsel_change2i_article.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.settingsel_change2i_delete = QLabel(self.settings_group)
        self.settingsel_change2i_delete.setObjectName(u"settingsel_change2i_delete")
        self.settingsel_change2i_delete.setGeometry(QRect(600, 350, 181, 31))
        self.settingsel_change2i_delete.setFont(font)
        self.settingsel_change2i_delete.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gl_setup_text = QLabel(self.centralwidget)
        self.gl_setup_text.setObjectName(u"gl_setup_text")
        self.gl_setup_text.setGeometry(QRect(120, 100, 1031, 71))
        self.gl_setup_text.setFont(font1)
        self.gl_setup_text.setMouseTracking(True)
        self.gl_setup_text.setAlignment(Qt.AlignCenter)
        self.gl_setup_path_show = QLineEdit(self.centralwidget)
        self.gl_setup_path_show.setObjectName(u"gl_setup_path_show")
        self.gl_setup_path_show.setGeometry(QRect(100, 250, 791, 61))
        font2 = QFont()
        font2.setPointSize(17)
        self.gl_setup_path_show.setFont(font2)
        self.gl_setup_path_sel = QPushButton(self.centralwidget)
        self.gl_setup_path_sel.setObjectName(u"gl_setup_path_sel")
        self.gl_setup_path_sel.setGeometry(QRect(974, 252, 171, 61))
        self.gl_setup_path_sel.setFont(font2)
        self.gl_setup_path_sel.setMouseTracking(True)
        self.bgp_show = QLabel(self.centralwidget)
        self.bgp_show.setObjectName(u"bgp_show")
        self.bgp_show.setGeometry(QRect(0, 40, 1281, 720))
        self.bgp_show.setMouseTracking(True)
        self.gl_setup_confirm = QPushButton(self.centralwidget)
        self.gl_setup_confirm.setObjectName(u"gl_setup_confirm")
        self.gl_setup_confirm.setGeometry(QRect(540, 410, 191, 71))
        self.gl_setup_confirm.setFont(font2)
        self.gl_setup_confirm.setMouseTracking(True)
        self.modesel = QComboBox(self.centralwidget)
        self.modesel.addItem("")
        self.modesel.addItem("")
        self.modesel.addItem("")
        self.modesel.addItem("")
        self.modesel.addItem("")
        self.modesel.setObjectName(u"modesel")
        self.modesel.setGeometry(QRect(850, 540, 391, 51))
        self.modesel.setFont(font2)
        self.modesel.setMaxVisibleItems(4)
        self.modesel.setInsertPolicy(QComboBox.InsertAtBottom)
        self.mode_set = QLabel(self.centralwidget)
        self.mode_set.setObjectName(u"mode_set")
        self.mode_set.setGeometry(QRect(1063, 620, 181, 61))
        self.mode_set.setFont(font2)
        self.mode_set.setAlignment(Qt.AlignCenter)
        self.mode_set_done = QLabel(self.centralwidget)
        self.mode_set_done.setObjectName(u"mode_set_done")
        self.mode_set_done.setGeometry(QRect(530, 630, 231, 41))
        self.start_game = QLabel(self.centralwidget)
        self.start_game.setObjectName(u"start_game")
        self.start_game.setGeometry(QRect(823, 620, 211, 61))
        self.start_launcher = QLabel(self.centralwidget)
        self.start_launcher.setObjectName(u"start_launcher")
        self.start_launcher.setGeometry(QRect(533, 620, 261, 61))
        self.start_bwiki = QLabel(self.centralwidget)
        self.start_bwiki.setObjectName(u"start_bwiki")
        self.start_bwiki.setGeometry(QRect(1030, 700, 131, 41))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 60, 1241, 631))
        self.bwiki_webview = QVBoxLayout(self.verticalLayoutWidget)
        self.bwiki_webview.setObjectName(u"bwiki_webview")
        self.bwiki_webview.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.bgp_show.raise_()
        self.win_con.raise_()
        self.gl_setup_text.raise_()
        self.gl_setup_path_show.raise_()
        self.gl_setup_path_sel.raise_()
        self.gl_setup_confirm.raise_()
        self.modesel.raise_()
        self.mode_set.raise_()
        self.start_game.raise_()
        self.start_launcher.raise_()
        self.settings_group.raise_()
        self.mode_set_done.raise_()
        self.start_bwiki.raise_()
        self.verticalLayoutWidget.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u542f\u52a8\u5668", None))
        self.win_con.setText("")
        self.settings_group.setTitle("")
        self.settings.setText("")
        self.setting_sel.setText("")
        self.setting_exit.setText("")
        self.settingsel_path.setText("")
        self.settingsel_path_bgp.setText("")
        self.settingsel_path_bgp_show.setText("")
        self.settingsel_path_bgp_selbt.setText("")
        self.settingsel_path_gl.setText("")
        self.settingsel_path_gl_show.setText("")
        self.settingsel_path_gl_selbt.setText("")
        self.settingsel_path_gs.setText("")
        self.settingsel_path_gs_show.setText("")
        self.settingsel_path_gs_selbt.setText("")
        self.settingsel_change2i.setText("")
        self.settingsel_change2i_zip.setText("")
        self.settingsel_change2i_zip_show.setText(QCoreApplication.translate("MainWindow", u"\u672a\u9009\u62e9", None))
        self.settingsel_change2i_zip_selbt.setText("")
        self.settingsel_change2i_selbt.setText("")
        self.settingsel_change2i_download.setText("")
        self.settingsel_change2i_article.setText("")
        self.settingsel_change2i_delete.setText("")
        self.gl_setup_text.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u6e38\u620f\u542f\u52a8\u5668\u5b89\u88c5\u8def\u5f84", None))
        self.gl_setup_path_sel.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9", None))
        self.bgp_show.setText("")
        self.gl_setup_confirm.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4", None))
        self.modesel.setItemText(0, QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4", None))
        self.modesel.setItemText(1, QCoreApplication.translate("MainWindow", u"\u56fd\u670d\uff08\u5b98\u670d\uff09", None))
        self.modesel.setItemText(2, QCoreApplication.translate("MainWindow", u"\u56fd\u670d\uff08\u5b98\u670d\uff09+ taptap", None))
        self.modesel.setItemText(3, QCoreApplication.translate("MainWindow", u"Bilibili\u670d\uff08\u6e20\u9053\u670d\uff09", None))
        self.modesel.setItemText(4, QCoreApplication.translate("MainWindow", u"\u56fd\u9645\u670d", None))

        self.mode_set.setText("")
        self.mode_set_done.setText("")
        self.start_game.setText("")
        self.start_launcher.setText("")
        self.start_bwiki.setText("")







from PySide2.QtWidgets import QMainWindow,QApplication,QFileDialog,QMessageBox
from PySide2.QtGui import QPixmap,QIcon,QMovie#,QImage#QCursor#,QMouseEvent
from PySide2.QtCore import Qt,QTimer,QObject
from PySide2.QtWebEngineWidgets import QWebEngineView
#import sys
from os import listdir,startfile,chdir,getcwd,rename,remove,startfile
from psutil import pids,Process
from shutil import copy,rmtree
from ctypes import windll
from zipfile import ZipFile
#import win32com.client
import webbrowser
#from cv2 import CAP_PROP_FPS,VideoCapture,CAP_PROP_FRAME_COUNT,CAP_PROP_POS_FRAMES,cvtColor,COLOR_BGR2RGB
#import cv2
#from ui_mw_v11 import Ui_MainWindow



class mainwin(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #self.setMouseTracking(True)
        #self.detect_launched_1()
        self.main_uiitemsetup()
        self.main_itemsetup()
        self.ui_setup()
        self.logic_setup()
        self.show()

    def main_uiitemsetup(self):

        self.eventtype_setting=False
        self.eventtype_normal=False
        self.eventtype_leftmouse=False
        self.eventtype_glsetdone=False
        self.eventtype_allenable=True
        self.eventtype_exitenable=True
        self.eventtype_setting_path=False
        self.eventtype_setting_change2i=False
        self.eventtype_bwiki_webview=False

        # self.centralwidget.setMouseTracking(True)
        self.setMouseTracking(True)
        self.modesel.setMaxVisibleItems(5)
        #self.modesel.removeItem(4)

        self.uigroup_all=[self.bwiki_webview,self.start_bwiki,self.centralwidget,self.bgp_show,self.modesel,self.mode_set,self.start_game,self.start_launcher,self.mode_set_done,self.settings,self.setting_exit,self.settings_group,self.settingsel_path_gl,self.settingsel_change2i,self.settingsel_change2i_zip,self.settingsel_change2i_download,self.settingsel_change2i_article,self.settingsel_change2i_delete,self.settingsel_change2i_zip_selbt,self.settingsel_change2i_zip_show,self.settingsel_change2i_selbt,self.settingsel_path_gs,self.settingsel_path_gs_show,self.settingsel_path_gs_selbt,self.settingsel_path_gl_selbt,self.settingsel_path_gl_show,self.setting_sel,self.settingsel_path_bgp_show,self.settingsel_path_bgp_selbt,self.settingsel_path_bgp,self.settingsel_path,self.gl_setup_text,self.gl_setup_path_sel,self.gl_setup_path_show,self.gl_setup_confirm,self.win_con]
        self.uigroup_gl_setup=[self.gl_setup_text,self.gl_setup_path_sel,self.gl_setup_path_show,self.gl_setup_confirm]
        self.uigroup_daily_open=[self.modesel,self.mode_set,self.start_game,self.start_launcher]#self.bgp_show,
        self.uigroup_settings=[self.settings,self.setting_exit,self.settings_group,self.setting_sel,self.settingsel_path,self.settingsel_path_bgp_show,self.settingsel_path_bgp_selbt,self.settingsel_path_bgp,self.settingsel_path_gl,self.settingsel_path_gl_selbt,self.settingsel_path_gl_show,self.settingsel_path_gs,self.settingsel_path_gs_show,self.settingsel_path_gs_selbt,self.settingsel_change2i,self.settingsel_change2i_zip,self.settingsel_change2i_zip_selbt,self.settingsel_change2i_zip_show,self.settingsel_change2i_selbt]
        self.uigroup_settings_path=[self.settingsel_path_bgp_show,self.settingsel_path_bgp_selbt,self.settingsel_path_bgp,self.settingsel_path_gl,self.settingsel_path_gl_selbt,self.settingsel_path_gl_show,self.settingsel_path_gs,self.settingsel_path_gs_show,self.settingsel_path_gs_selbt]
        self.uigroup_settings_change2i=[self.settingsel_change2i_zip,self.settingsel_change2i_zip_selbt,self.settingsel_change2i_zip_show,self.settingsel_change2i_selbt,self.settingsel_change2i_download,self.settingsel_change2i_article,self.settingsel_change2i_delete]

        for i in self.uigroup_all:
            try:
                i.setMouseTracking(True)
            except:
                pass

        self.mode_set_done.setEnabled(False)
        self.mode_set_done.setVisible(False)
        self.verticalLayoutWidget.setEnabled(False)
        self.verticalLayoutWidget.setVisible(False)

        self.gl_setup_text.setPixmap(QPixmap("custom_launcher_sources\\gl_setup_text.png"))

        self.gl_setup_path_sel.clicked.connect(self.gl_path_sel)
        self.gl_setup_confirm.clicked.connect(self.gl_path_conf)
        self.modesel.currentIndexChanged.connect(self.modesel_event)

        self.scfile_exist=False
        self.bgp_timer = QTimer()
        self.bwiki_web=QWebEngineView()
        self.bwiki_web.setUrl("https://wiki.biligame.com/ys")
        self.bwiki_webview.addWidget(self.bwiki_web)

        self.dec_pro_timer=QTimer()
        self.dec_pro_timer.timeout.connect(self.detect_launched_1)
        self.dec_pro_timer.start(1000)

    def main_itemsetup(self):
        #self.game_source_path=".."
        #self.game_launcher_path=""
        #self.game_downloaded_path=""
        self.config_content_dict={}
        if "zp.txt" in listdir("custom_launcher_sources"):
            with open("custom_launcher_sources\\zp.txt","r") as f:
                zp=f.read()
            self.sources_path_in_zip=zp.split("\n")[0]
        else:
            self.sources_path_in_zip=""

    def ui_setup(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.bgp_show.setScaledContents(True)
        for i in self.uigroup_settings:
            i.setEnabled(False)
            i.setVisible(False)
        for i in self.uigroup_gl_setup:
            i.setEnabled(False)
            i.setVisible(False)
        for i in self.uigroup_daily_open:
            i.setVisible(True)
            i.setEnabled(True)
        if self.scfile_exist:
            self.win_con.setPixmap(QPixmap("custom_launcher_sources\\win_title_scfile.png"))
        else:
            self.win_con.setPixmap(QPixmap("custom_launcher_sources\\win_title.png"))
        with open("custom_launcher_sources\\launcher_config.ini","r") as f:
            config_content=f.read()
        self.config_content_dict={"launcher_bgp":config_content.split("launcher_bgp=")[-1].split("\n")[0],
                             "game_launcher_path":config_content.split("game_launcher_path=")[-1].split("\n")[0],
                             "game_downloaded_path":config_content.split("game_downloaded_path=")[-1].split("\n")[0],
                                  "org_gsini":config_content.split("org_gsini=")[-1].split("\n")[0],
                                  "now_mode":config_content.split("now_mode=")[-1].split("\n")[0],
                                  "file_type": config_content.split("file_type=")[-1].split("\n")[0],
                                  "zip_file":config_content.split("zip_file=")[-1].split("\n")[0]}
        #print(self.config_content_dict)
        self.mode_dict={1:["1","mihoyo","0",""],2:["1","mihoyo","1",""],3:["14","bilibili","0",""],4:["1","mihoyo","0",""]}
        try:
            if "launcher.exe" not in listdir(self.config_content_dict["game_launcher_path"]):
                self.config_content_dict["game_launcher_path"]=""
                self.write_ini()
        except:
            self.config_content_dict["game_launcher_path"] = ""
            self.write_ini()
        self.scfile_exist=self.check_scfile(self.config_content_dict["game_downloaded_path"])
        if self.config_content_dict["game_launcher_path"]=="":
            self.eventtype_glsetdone=False
            self.bgp_show.setPixmap(QPixmap("custom_launcher_sources\\bgp_org.png"))
            for i in self.uigroup_daily_open:
                i.setEnabled(False)
                i.setVisible(False)
            for i in self.uigroup_gl_setup:
                i.setVisible(True)
                i.setEnabled(True)
            self.gl_setup_path_show.setEnabled(False)
            self.gl_setup_confirm.setEnabled(False)
            self.start_bwiki.setEnabled(False)
            self.start_bwiki.setVisible(False)
        else:
            self.eventtype_glsetdone=True
            self.ui_setup_2()

    def logic_setup(self):
        pass
        #self.mousePosDetect_count_1()

    def gl_path_sel(self):
        sel_file, _ = QFileDialog.getOpenFileName(self, "选择启动器", "","launcher.exe (launcher.exe)")
        if sel_file and sel_file!="":
            self.gl_setup_confirm.setEnabled(True)
            self.gl_setup_path_show.setText(sel_file)
        # sel_path = QFileDialog.getExistingDirectory(self, "选择游戏启动器安装文件夹")
        # self.gl_setup_path_show.setText(sel_path)
        # if sel_path!="":
        #     self.gl_setup_confirm.setEnabled(True)

    def gl_path_conf(self):
        if self.gl_setup_path_show.text()!="":
            try:
                #if "launcher.exe" in listdir(self.gl_setup_path_show.text()):
                for i in self.uigroup_gl_setup:
                    i.setEnabled(False)
                    i.setVisible(False)
                for i in self.uigroup_daily_open:
                    i.setVisible(True)
                    i.setEnabled(True)
                self.start_bwiki.setVisible(True)
                self.start_bwiki.setEnabled(True)
                self.config_content_dict["game_launcher_path"] = path.split(self.gl_setup_path_show.text())[0]
                self.write_ini()
                self.eventtype_glsetdone = True
                self.ui_setup_2()
                # else:
                #     QMessageBox().warning(self,"注意","没有找到 launcher.exe ，请确保路径正确")
            except:
                QMessageBox().critical(self,"错误","程序错误")

    def ui_setup_2(self):
        self.eventtype_normal=True
        self.modesel.setCurrentIndex(int(self.config_content_dict["now_mode"]))
        self.settings.setPixmap(QPixmap("custom_launcher_sources\\settings.png"))
        self.setting_exit.setPixmap(QPixmap("custom_launcher_sources\\setting_exit.png"))
        #self.settingsel_change2i_selbt.setPixmap(QPixmap("custom_launcher_sources\\"))
        self.settingsel_change2i_zip_selbt.setPixmap(QPixmap("custom_launcher_sources\\settingsel_change2i_zip_selbt.png"))
        with open(f"{self.config_content_dict['game_launcher_path']}\\config.ini","r") as f:
            gl_config_content=f.read()
        gs_type=gl_config_content.split("game_start_name=")[-1].split("\n")[0]
        if gs_type=="YuanShen.exe":
            self.settingsel_change2i_zip.setPixmap(QPixmap("custom_launcher_sources\\settingsel_change2i_zip_c2i.png"))
            change_type="GenshinImpact.exe"
        else:
            self.settingsel_change2i_zip.setPixmap(QPixmap("custom_launcher_sources\\settingsel_change2i_zip_i2c.png"))
            change_type="YuanShen.exe"
        bgp=gl_config_content.split("game_dynamic_bg_name=")[-1].split("\n")[0]
        if self.config_content_dict["launcher_bgp"]=="" and self.config_content_dict["game_launcher_path"]=="":
            self.bgp_show.setPixmap(QPixmap("custom_launcher_sources\\bgp_org.png"))
        elif self.config_content_dict["launcher_bgp"]=="" and self.config_content_dict["game_launcher_path"]!="":
            self.bgp_show.setPixmap(QPixmap(f"{self.config_content_dict['game_launcher_path']}\\bg\\{bgp}"))
        else:
            self.show_background(self.config_content_dict["launcher_bgp"])
            #self.bgp_show.setPixmap(QPixmap())
        if "icchange" in listdir("custom_launcher_sources"):
            if self.config_content_dict["game_downloaded_path"]!="" and "config.ini" in listdir("custom_launcher_sources\\icchange") and change_type in listdir("custom_launcher_sources\\icchange"):
                self.settingsel_change2i_zip_show.setText("已选择")
            else:
                self.settingsel_change2i_zip_show.setText("未选择")
        else:
            self.settingsel_change2i_zip_show.setText("未选择")
        self.settingsel_change2i.setPixmap(QPixmap("custom_launcher_sources\\settingsel_change2i.png"))
        self.settingsel_path_bgp_show.setText(self.config_content_dict["launcher_bgp"])
        self.settingsel_path_gl.setPixmap(QPixmap("custom_launcher_sources\\settingsel_path_gl.png"))
        self.settingsel_path_gl_show.setPixmap(QPixmap("custom_launcher_sources\\settingsel_path_gl_show.png"))
        self.settingsel_path_gs.setPixmap(QPixmap("custom_launcher_sources\\settingsel_path_gs.png"))
        if self.config_content_dict["game_downloaded_path"]=="":
            self.settingsel_path_gs_show.setPixmap(QPixmap("custom_launcher_sources\\settingsel_path_gs_show.png"))
        else:
            self.settingsel_path_gs_show.setText(self.config_content_dict["game_downloaded_path"])
        self.settingsel_path_gl_show.setText(self.config_content_dict["game_launcher_path"])
        self.setting_sel.setPixmap(QPixmap("custom_launcher_sources\\setting_sel.png"))
        self.settingsel_path.setPixmap(QPixmap("custom_launcher_sources\\settingsel_path_touch.png"))
        self.settingsel_path_bgp.setPixmap(QPixmap("custom_launcher_sources\\settingsel_path_bgp.png"))
        self.settingsel_path_bgp_selbt.setPixmap(QPixmap("custom_launcher_sources\\settingsel_path_bgp_selbt.png"))
        if self.config_content_dict["launcher_bgp"]=="":
            self.settingsel_path_bgp_show.setPixmap(QPixmap("custom_launcher_sources\\settingsel_path_bgp_show.png"))
        else:
            self.settingsel_path_bgp_show.setText(self.config_content_dict["launcher_bgp"])
        self.mode_set_done.setPixmap(QPixmap("custom_launcher_sources\\mode_set_done.png"))
        self.mode_set.setPixmap(QPixmap("custom_launcher_sources\\mode_set.png"))
        self.start_game.setPixmap(QPixmap("custom_launcher_sources\\start_game.png"))
        self.start_launcher.setPixmap(QPixmap("custom_launcher_sources\\start_launcher.png"))
        self.start_bwiki.setPixmap(QPixmap("custom_launcher_sources\\bwiki_web.png"))

    def settings_show(self,mode):
        if mode==True:
            #print(self.setting_exit.x())
            self.eventtype_normal=False
            self.eventtype_setting=True
            self.eventtype_setting_path=True
            for i in self.uigroup_settings:
                i.setVisible(True)
                i.setEnabled(True)
            for i in self.uigroup_settings_change2i:
                i.setEnabled(False)
                i.setVisible(False)
            if "icchange" in listdir("custom_launcher_sources"):
                self.settingsel_path_gl_selbt.setVisible(False)
                self.settingsel_path_gs_selbt.setVisible(False)
        else:
            for i in self.uigroup_settings:
                i.setEnabled(False)
                i.setVisible(False)
                self.eventtype_setting_path=False
                self.eventtype_setting_change2i=False
                self.eventtype_setting = False
                self.eventtype_normal = True

    def sel_bgp(self):
        # op=QFileDialog.Options()
        # op |= QFileDialog.DontUseNativeDialog
        sel_file,_ = QFileDialog.getOpenFileName(self, "选择背景图片","","所有类型 (*.*);;PNG File (*.png);;JPEG File (*.jpg,*.jpeg,*.jpe,*.jfif);;GIF File (*.gif)")#,options=op)#"PNG Files (*.png);;JPEG Files (*.jpg,*.jpeg,*.jpe,*.jfif)")
        if sel_file and sel_file!="":
            log=self.show_background(sel_file)
            if log["error"]==False:
                self.config_content_dict["launcher_bgp"]=sel_file
                #self.bgp_show.setPixmap(QPixmap(self.config_content_dict["launcher_bgp"]))
                self.settingsel_path_bgp_show.setText(self.config_content_dict["launcher_bgp"])
                self.write_ini()
            else:
                QMessageBox().critical(self,"错误","发生错误")
        else:
            self.bgp_timer.stop()
            self.config_content_dict["launcher_bgp"] = sel_file
            self.settingsel_path_bgp_show.setPixmap(QPixmap("custom_launcher_sources\\settingsel_path_bgp_show.png"))
            if self.config_content_dict["launcher_bgp"] == "" and self.config_content_dict["game_launcher_path"] == "":
                self.bgp_show.setPixmap(QPixmap("custom_launcher_sources\\bgp_org.png"))
            elif self.config_content_dict["launcher_bgp"] == "" and self.config_content_dict[
                "game_launcher_path"] != "":
                with open(f"{self.config_content_dict['game_launcher_path']}\\config.ini", "r") as f:
                    gl_config_content = f.read()
                bgp = gl_config_content.split("game_dynamic_bg_name=")[-1].split("\n")[0]
                self.bgp_show.setPixmap(QPixmap(f"{self.config_content_dict['game_launcher_path']}\\bg\\{bgp}"))
            else:
                self.bgp_show.setPixmap(QPixmap(self.config_content_dict["launcher_bgp"]))
            self.write_ini()
            self.settingsel_path_bgp_show.setText(self.config_content_dict["launcher_bgp"])

    def write_ini(self):
        with open("custom_launcher_sources\\launcher_config.ini", "w") as f:
            for i in self.config_content_dict:
                f.write(f"{i}={self.config_content_dict[i]}\n")

    def sel_gl(self):
        sel_file, _ = QFileDialog.getOpenFileName(self, "选择启动器", "",
                                                  "launcher.exe (launcher.exe)")  # ,options=op)#"PNG Files (*.png);;JPEG Files (*.jpg,*.jpeg,*.jpe,*.jfif)")
        if sel_file and sel_file != "":
            self.config_content_dict["game_downloaded_path"] = ""
            self.settingsel_path_gs_show.setPixmap(QPixmap("custom_launcher_sources\\settingsel_path_gs_show.png"))
            sel_file=path.split(sel_file)[0]
            self.config_content_dict["game_launcher_path"] = sel_file
            self.config_content_dict["org_gsini"] = ""
            if "icchange" in listdir("custom_launcher_sources"):  # path.exists("custom_launcher_sources\\icchange"):
                if listdir("custom_launcher_sources\\icchange"):
                    self.del_c_s()
                # if "icchange" in listdir("custom_launcher_sources"):
                rmtree("custom_launcher_sources\\icchange")
            with open("custom_launcher_sources\\zpfps", "w") as f:
                f.write("")
            self.settingsel_change2i_zip_show.setText("未选择")
            self.settingsel_path_gl_show.setText(self.config_content_dict["game_launcher_path"])
            self.write_ini()

    def sel_gs(self):
        with open(f'{self.config_content_dict["game_launcher_path"]}\\config.ini',"r") as f:
            inict=f.read()
        selfn=inict.split("game_start_name=")[-1].split("\n")[0]
        sel_file, _ = QFileDialog.getOpenFileName(self, "选择游戏本体", "",f"{selfn} ({selfn})")
        if sel_file and sel_file != "":
            if "icchange" in listdir("custom_launcher_sources"):  # path.exists("custom_launcher_sources\\icchange"):
                if listdir("custom_launcher_sources\\icchange"):
                    self.del_c_s()
                # if "icchange" in listdir("custom_launcher_sources"):
                rmtree("custom_launcher_sources\\icchange")
            with open("custom_launcher_sources\\zpfps", "w") as f:
                f.write("")
            self.settingsel_change2i_zip_show.setText("未选择")
            sel_file = path.split(sel_file)[0]
            if selfn=="YuanShen.exe":
                if "PCGameSDK.dll" not in sel_file+"/YuanShen_Data/Plugins":
                    copy("custom_launcher_sources\\run.dll",f"{sel_file}\\YuanShen_Data\\Plugins\\PCGameSDK.dll")
            else:
                if "PCGameSDK.dll.backupc" not in sel_file+"/GenshinImpact_Data/Plugins":
                    copy("custom_launcher_sources\\run.dll",f"{sel_file}\\GenshinImpact_Data\\Plugins\\PCGameSDK.dll.backupc")
            self.config_content_dict["game_downloaded_path"] = sel_file
            self.settingsel_path_gs_show.setText(self.config_content_dict["game_downloaded_path"])
            if selfn=="YuanShen.exe":
                self.config_content_dict["org_gsini"]=self.set_org_mode(sel_file)
            else:
                self.config_content_dict["org_gsini"] ="4"
            self.write_ini()
            self.modesel.setCurrentIndex(0)

    def sel_zip(self):
        if self.config_content_dict["game_downloaded_path"]=="":
            QMessageBox().warning(self,"注意","请先设置 游戏资源")
        else:
            with open(f'{self.config_content_dict["game_launcher_path"]}\\config.ini',"r") as f:
                inict=f.read()
            selfn=inict.split("game_start_name=")[-1].split("\n")[0]
            with open(f'{self.config_content_dict["game_downloaded_path"]}\\config.ini') as f:
                inict=f.read()
            orgfile_ver=inict.split("game_version=")[-1].split("\n")[0]
            sel_file, _ = QFileDialog.getOpenFileName(self, "选择转服压缩包", "", "转服压缩包 (*.zip)")
            if sel_file and sel_file!="":
                #with ZipFile(sel_file,"r") as f:
                zip_file=ZipFile(sel_file,"r")
                files_in_zip=zip_file.namelist()
                if selfn=="YuanShen.exe":
                    secfn="GenshinImpact.exe"
                else:
                    secfn="YuanShen.exe"
                #print(files_in_zip,"\n",self.sources_path_in_zip+"config.ini","\n",self.sources_path_in_zip+secfn)
                if self.sources_path_in_zip+"config.ini" in files_in_zip and self.sources_path_in_zip+secfn in files_in_zip:
                    zip_inict=str(zip_file.read(self.sources_path_in_zip+"config.ini"))
                    if zip_inict.split("game_version=")[-1].split("\\r\\n")[0]==orgfile_ver:
                        zip_file.close()
                        self.sel_zip_2(sel_file)
                    else:
                        zip_file.close()
                        QMessageBox().warning(self,"注意","转服压缩包不适用")
                    #print(zip_inict.split("game_version=")[-1].split("\\r\\n")[0],orgfile_ver)
                else:
                    zip_file.close()
                    QMessageBox().warning(self, "注意", "转服压缩包不适用")
            else:
                if "icchange" in listdir("custom_launcher_sources"):#path.exists("custom_launcher_sources\\icchange"):
                    if listdir("custom_launcher_sources\\icchange"):
                        self.del_c_s()
                #if "icchange" in listdir("custom_launcher_sources"):
                    rmtree("custom_launcher_sources\\icchange")
                with open("custom_launcher_sources\\zpfps", "w") as f:
                    f.write("")
                self.settingsel_change2i_zip_show.setText("未选择")

    def sel_zip_2(self,zip_file_path):
        zip_file=ZipFile(zip_file_path,"r")
        afne=zip_file.namelist()
        afn = zip_file.namelist()
        if self.sources_path_in_zip != "":
            for i in afne:
                if ".txt" in i.split(self.sources_path_in_zip)[-1] and "/" not in i.split(self.sources_path_in_zip)[-1]:
                    afn.remove(i)
                elif i[-1] == "/" or i[-1] == "\\":
                    afn.remove(i)
                else:
                    # f.write(i.split(self.sources_path_in_zip)[-1] + "\n")
                    pass
        else:
            for i in afne:
                if ".txt" in i and "/" not in i:
                    afn.remove(i)
                elif i[-1] == "/" or i[-1] == "\\":
                    afn.remove(i)
                else:
                    #f.write(i + "\n")
                    pass
        with open("custom_launcher_sources\\zpfps","w") as f:
            if self.sources_path_in_zip != "":
                for i in afn:
                    f.write(i.split(self.sources_path_in_zip)[-1] + "\n")
            else:
                for i in afn:
                    f.write(i + "\n")
        zip_file.extractall("custom_launcher_sources\\icchange\\")
        zip_file.close()
        if self.sources_path_in_zip=="":
            p=""
        else:
            p=f"\\{self.sources_path_in_zip[0:-1]}"
        for i in listdir(f"custom_launcher_sources\\icchange{p}"):
            if ".txt" in i and "/" not in i:
                remove(f"custom_launcher_sources\\icchange{p}\\{i}")
                break
        self.copy_cs_f()
        self.settingsel_change2i_zip_show.setText("已选择")

    def write_gsini(self,ent):
        ch,cps,sbc,_=ent
        if "config.ini.backup" not in listdir(self.config_content_dict['game_downloaded_path']):
            copy(f"{self.config_content_dict['game_downloaded_path']}\\config.ini",f"{self.config_content_dict['game_downloaded_path']}\\config.ini.backup")
        # if str(ch)=="14":
        #     if "PCGameSDK.dll" not in listdir(f"{self.config_content_dict['game_downloaded_path']}\\YuanShen_Data\\Plugins"):
        #         copy("custom_launcher_sources\\run.dll",f"{self.config_content_dict['game_downloaded_path']}\\YuanShen_Data\\Plugins\\PCGameSDK.dll")
        with open(f"{self.config_content_dict['game_downloaded_path']}\\config.ini","r") as f:
            org_content=f.read()
        #change_content=org_content.split("channel="+org_content.split("channel=")[-1].split("\n")[0])[0]+"channel="+str(ch)+"\n"
        sp_content=org_content.split("\n")
        # if self.config_content_dict["org_gsini"] == "":
        #     org_inict=[]
        #     for i in sp_content:
        #         if "channel=" in i:
        #             org_inict.append(i.split("channel=")[-1])
        #         elif "cps=" in i:
        #             org_inict.append(i.split("cps=")[-1])
        #         elif "sub_channel=" in i:
        #             org_inict.append(i.split("sub_channel=")[-1])
        #     self.config_content_dict["game_downloaded_path"]=org_inict[0]+";/;"+org_inict[1]+";/;"+org_inict[2]
        #     self.write_ini()
        change_content=""
        for i in sp_content:
            if "sub_channel=" in i:
                change_content += "sub_channel=" + str(sbc)
            elif "cps=" in i:
                change_content+="cps="+str(cps)
            elif "channel=" in i:
                change_content+="channel="+str(ch)
            else:
                change_content+=i
            change_content+="\n"
        with open(f"{self.config_content_dict['game_downloaded_path']}\\config.ini", "w") as f:
            f.write(change_content)

    def set_org_mode(self, gsp):
        # print(gsp)
        if "config.ini.backup" not in listdir(gsp):
            copy(f"{gsp}\\config.ini", f"{gsp}\\config.ini.backup")
        with open(f"{gsp}\\config.ini.backup", "r") as f:
            ogc = f.read()
        sp_content = ogc.split("\n")
        org_inict = []
        nch=""
        for i in sp_content:
            if "sub_channel=" in i:
                org_inic = i.split("sub_channel=")[-1]
                # org_inict += ";/;"
                if nch=="14":
                    org_inic="0"
                org_inict.append(org_inic)
            elif "cps=" in i:
                org_inic = i.split("cps=")[-1]
                # org_inict += ";/;"
                org_inict.append(org_inic)
            elif "channel=" in i:
                org_inic = i.split("channel=")[-1]
                # org_inict += ";/;"
                org_inict.append(org_inic)
                nch=org_inic
        org_inict.append("")
        return self.get_index(org_inict)

    def get_index(self, lst):
        b = None
        for i in self.mode_dict:
            if lst == self.mode_dict[i]:
                b = i
        return b

    def set_nowmode(self):
        if self.config_content_dict["game_downloaded_path"]=="":
            QMessageBox().warning(self,"注意","请先设置 游戏资源")
        else:
            md = self.modesel.currentIndex()
            # print(md) 
            g1 = [1, 2, 3]
            g2 = [4]
            snm = str(md)
            if md == 0:
                #self.config_content_dict["now_mode"] = str(md)
                md = int(self.config_content_dict["org_gsini"])
            if int(self.config_content_dict["now_mode"]) == 0:
                nd = int(self.config_content_dict["org_gsini"])
            else:
                nd = int(self.config_content_dict["now_mode"])
            if nd in g1:
                now_s = "c"
            else:
                now_s = "i"
            if md in g1:
                tar_s = "c"
                tar_fn = "YuanShen"
            else:
                tar_s = "i"
                tar_fn = "GenshinImpact"
            #self.config_content_dict["now_mode"]=snm
            if tar_s == now_s:
                # print("equ")
                #self.write_ini()
                if tar_s=="c":
                    if md == 0:
                        ent = self.mode_dict[int(self.config_content_dict["org_gsini"])]
                    else:
                        ent = self.mode_dict[md]
                    self.write_gsini(ent)
                self.mode_set_done.setVisible(True)
                self.mode_set_done.setEnabled(True)
                self.config_content_dict["now_mode"] = snm
                self.write_ini()
                QTimer().singleShot(2000,self.set_nowmode_2)
            else:
                # self.c_s(md)
                #self.write_ini()
                if self.c_s(md) == True:
                    # print("in")
                    if tar_s == "c":
                        if md == 0:
                            ent = self.mode_dict[int(self.config_content_dict["org_gsini"])]
                        else:
                            ent = self.mode_dict[md]
                        self.write_gsini(ent)
                        self.start_launcher.setVisible(True)
                        self.start_launcher.setEnabled(True)
                    self.mode_set_done.setVisible(True)
                    self.mode_set_done.setEnabled(True)
                    self.config_content_dict["now_mode"] = snm
                    self.write_ini()
                    QTimer().singleShot(2000,self.set_nowmode_2)
                else:
                    print(f"self.c_s({md}) returns False")
                    #self.mode_set_done.setVisible(True)
                    #self.mode_set_done.setEnabled(True)
                    self.set_nowmode_2()
            # try:
            #     md = self.modesel.currentIndex()
            #     # print(md)
            #     g1 = [1, 2, 3]
            #     g2 = [4]
            #
            #     if md == 0:
            #         md = int(self.config_content_dict["org_gsini"])
            #     if int(self.config_content_dict["now_mode"]) == 0:
            #         nd = int(self.config_content_dict["org_gsini"])
            #     else:
            #         nd = int(self.config_content_dict["now_mode"])
            #     if nd in g1:
            #         now_s = "c"
            #     else:
            #         now_s = "i"
            #     if md in g1:
            #         tar_s = "c"
            #         tar_fn = "YuanShen"
            #     else:
            #         tar_s = "i"
            #         tar_fn = "GenshinImpact"
            #     if tar_s == now_s:
            #         # print("equ")
            #         pass
            #     else:
            #         # self.c_s(md)
            #         if self.c_s(md) == True:
            #             # print("in")
            #             pass
            #         else:
            #             pass
            #     self.start_launcher.setVisible(True)
            #     self.start_launcher.setEnabled(True)
            #     if self.config_content_dict["org_gsini"]=="":
            #         self.config_content_dict["org_gsini"]=self.set_org_mode(self.config_content_dict["game_downloaded_path"])
            #         self.write_ini()
            #     md=self.modesel.currentIndex()
            #     #print(md)
            #     self.config_content_dict["now_mode"]=str(md)
            #     self.write_ini()
            #     if md==0:
            #         ent=self.mode_dict[int(self.config_content_dict["org_gsini"])]
            #     else:
            #         ent=self.mode_dict[md]
            #
            #     self.write_gsini(ent)
            #     self.mode_set_done.setPixmap(QPixmap("custom_launcher_sources\\mode_set_done.png"))
            #     self.mode_set_done.setVisible(True)
            #     self.mode_set_done.setEnabled(True)
            #     QTimer().singleShot(2000,self.set_nowmode_2)
            # except:
            #     QMessageBox().critical(self,"错误","程序错误")

    def set_nowmode_2(self):
        self.mode_set_done.setEnabled(False)
        self.mode_set_done.setVisible(False)

    def start_gl(self):
        startfile(self.config_content_dict["game_launcher_path"]+"/launcher.exe")
        self.start_launcher.setPixmap(QPixmap("custom_launcher_sources\\start_launcher_done.png"))
        QTimer().singleShot(2000, self.start_gl_2)

    # def start_g(self):
    #     if self.config_content_dict["game_downloaded_path"]=="":
    #         QMessageBox().warning(self,"注意","请先设置 游戏资源")
    #     else:
    #         try:
    #             md = self.modesel.currentIndex()
    #             g1 = [1, 2, 3]
    #             g2 = [4]
    #
    #             if md == 0:
    #                 md = int(self.config_content_dict["org_gsini"])
    #             if int(self.config_content_dict["now_mode"]) in g1:
    #                 now_s = "c"
    #             else:
    #                 now_s = "i"
    #             if md in g1:
    #                 tar_s = "c"
    #                 tar_fn = "YuanShen"
    #             else:
    #                 tar_s = "i"
    #                 tar_fn = "GenshinImpact"
    #             if tar_s == now_s:
    #                 self.start_g_1_1()
    #             else:
    #                 #self.c_s(md)
    #                 if self.c_s(md)==True:
    #                     self.start_g_1_1()
    #             #QTimer().singleShot(500,self.start_g_1_1)
    #
    #         except:
    #             QMessageBox().critical(self,"错误","程序错误")
    def start_g(self):
        if self.config_content_dict["game_downloaded_path"]=="":
            QMessageBox().warning(self,"注意","请先设置 游戏资源")
        else:
            md = self.modesel.currentIndex()
            #print(md)
            g1 = [1, 2, 3]
            g2 = [4]

            if md == 0:
                md = int(self.config_content_dict["org_gsini"])
            if int(self.config_content_dict["now_mode"])==0:
                nd=int(self.config_content_dict["org_gsini"])
            else:
                nd=int(self.config_content_dict["now_mode"])
            if nd in g1:
                now_s = "c"
            else:
                now_s = "i"
            if md in g1:
                tar_s = "c"
                tar_fn = "YuanShen"
            else:
                tar_s = "i"
                tar_fn = "GenshinImpact"
            if tar_s == now_s:
                #print("equ")
                self.start_g_1_1()
            else:
                # self.c_s(md)
                if self.c_s(md) == True:
                    #print("in")
                    self.start_g_1_1()
                # QTimer().singleShot(500,self.start_g_1_1)

    def start_g_1_1(self):
        md = self.modesel.currentIndex()
        g1=[1,2,3]
        g2=[4]
        snm=str(md)
        if md == 0:
            #self.config_content_dict["now_mode"] = str(md)
            md = int(self.config_content_dict["org_gsini"])
        if md in g1:
            tar_s = "c"
            tar_fn = "YuanShen"
            self.start_launcher.setVisible(True)
            self.start_launcher.setEnabled(True)
        else:
            tar_s = "i"
            tar_fn = "GenshinImpact"
            self.start_launcher.setEnabled(False)
            self.start_launcher.setVisible(False)
        if self.config_content_dict["org_gsini"] == "":
            with open(f'{self.config_content_dict["game_launcher_path"]}\\config.ini', "r") as f:
                inict = f.read()
            selfn = inict.split("game_start_name=")[-1].split("\n")[0]
            if selfn=="YuanShen.exe":
                self.config_content_dict["org_gsini"]=self.set_org_mode(self.config_content_dict["game_downloaded_path"])
            else:
                self.config_content_dict["org_gsini"] ="4"
            # self.config_content_dict["org_gsini"] = self.set_org_mode(
            #     self.config_content_dict["game_downloaded_path"])
            self.write_ini()

        # print(md)
        self.config_content_dict["now_mode"] = snm
        self.write_ini()
        if md == 0:
            ent = self.mode_dict[int(self.config_content_dict["org_gsini"])]
        else:
            ent = self.mode_dict[md]
        self.write_gsini(ent)
        org_dir = getcwd()
        chdir(self.config_content_dict["game_downloaded_path"])
        startfile(self.config_content_dict["game_downloaded_path"] + "/" + tar_fn + ".exe")
        chdir(org_dir)
        self.start_game.setPixmap(QPixmap("custom_launcher_sources\\start_game_done.png"))
        QTimer().singleShot(2000, self.start_g_2)

    def start_g_2(self):
        self.start_game.setPixmap(QPixmap("custom_launcher_sources\\start_game.png"))

    def start_gl_2(self):
        self.start_launcher.setPixmap(QPixmap("custom_launcher_sources\\start_launcher.png"))

    def settingsel_path_event(self,mode):
        if mode==True:
            #self.eventtype_setting_change2i=False
            self.eventtype_setting_path=True
            self.settingsel_path.setPixmap(QPixmap("custom_launcher_sources\\settingsel_path_touch.png"))
            for i in self.uigroup_settings_path:
                i.setVisible(True)
                i.setEnabled(True)
            if "icchange" in listdir("custom_launcher_sources"):
                self.settingsel_path_gl_selbt.setVisible(False)
                self.settingsel_path_gs_selbt.setVisible(False)
        else:
            self.eventtype_setting_path = False
            self.settingsel_path.setPixmap(QPixmap("custom_launcher_sources\\settingsel_path.png"))
            for i in self.uigroup_settings_path:
                i.setEnabled(False)
                i.setVisible(False)

    def settingsel_change2i_event(self,mode):
        if mode == True:
            self.eventtype_setting_change2i = True
            self.settingsel_change2i.setPixmap(QPixmap("custom_launcher_sources\\settingsel_change2i_touch.png"))
            for i in self.uigroup_settings_change2i:
                i.setVisible(True)
                i.setEnabled(True)
        else:
            self.eventtype_setting_change2i = False
            self.settingsel_change2i.setPixmap(QPixmap("custom_launcher_sources\\settingsel_change2i.png"))
            for i in self.uigroup_settings_change2i:
                i.setEnabled(False)
                i.setVisible(False)

    def modesel_event(self):
        g1=[1,2,3]
        g2=[4]
        try:
            org_id=int(self.config_content_dict["org_gsini"])
            self.modesel_event_2(g1,g2,org_id)
        except:
            pass
    def modesel_event_2(self,g1,g2,org_id):
        if org_id in g1:
            org_gn="YuanShen"
            org_s="c"
        else:
            org_gn="GenshinImpact"
            org_s="i"
        selid=self.modesel.currentIndex()
        if selid==0:
            selid=org_id
        if selid in g1:
            tar_gn="YuanShen"
            tar_s="c"
        else:
            tar_gn="GenshinImpact"
            tar_s="i"
        if tar_s==org_s:
            # itg = [self.mode_set, self.start_launcher]
            # for i in itg:
            #     i.setVisible(True)
            #     i.setEnabled(True)
            self.mode_set.setVisible(True)
            self.mode_set.setEnabled(True)
            if org_gn+".exe" in listdir(self.config_content_dict["game_downloaded_path"]):
                self.start_launcher.setVisible(True)
                self.start_launcher.setEnabled(True)

        else:
            itg = [self.mode_set, self.start_launcher]
            for i in itg:
                i.setEnabled(False)
                i.setVisible(False)

        if tar_gn+".exe" in listdir(self.config_content_dict["game_downloaded_path"]) or tar_gn+".exe.backup"+tar_s in listdir(self.config_content_dict["game_downloaded_path"]):
            self.start_game.setVisible(True)
            self.start_game.setEnabled(True)
        else:
            self.start_game.setEnabled(False)
            self.start_game.setVisible(False)


    def del_c_s(self):
        with open("custom_launcher_sources\\zpfps","r") as f:
            zpfps=f.read()
        file_paths=zpfps.split("\n")
        if file_paths[-1]=="":
            file_paths.pop(-1)
        self.modesel.setCurrentIndex(0)

        g1 = [1, 2, 3]
        g2 = [4]
        gsp = self.config_content_dict["game_downloaded_path"]

        if int(self.config_content_dict["org_gsini"]) in g1:
            org_f = "YuanShen"
            zip_f = "GenshinImpact"
            zip_m = "i"
        else:
            org_f = "GenshinImpact"
            zip_f = "YuanShen"
            zip_m = "c"
        #if org_f+".exe" not in listdir(gsp):
        #    self.c_s(int(self.config_content_dict["org_gsini"]))
        self.set_nowmode()
        # g1 = [1, 2, 3]
        # g2 = [4]
        # gsp = self.config_content_dict["game_downloaded_path"]
        # if int(self.config_content_dict["org_gsini"]) in g1:
        #     org_f = "YuanShen"
        #     zip_f = "GenshinImpact"
        #     zip_m="i"
        # else:
        #     org_f = "GenshinImpact"
        #     zip_f = "YuanShen"
        #     zip_m="c"
        rename(gsp+"/"+org_f+"_Data",gsp+"/"+zip_f+"_Data")
        for i in file_paths:
            try:
                if self.sources_path_in_zip != "":
                    isp = i.split(self.sources_path_in_zip)[-1]
                else:
                    isp = i
                if isp[-13:]=="PCGameSDK.dll":
                    pass
                else:
                    remove(gsp+"/"+isp+".backup"+zip_m)
            except:
                pass
        rename(gsp + "/" + zip_f + "_Data",gsp + "/" + org_f + "_Data")

    def copy_cs_f(self):
        with open("custom_launcher_sources\\zpfps","r") as f:
            zpfps=f.read()
        file_paths=zpfps.split("\n")
        if file_paths[-1]=="":
            file_paths.pop(-1)
        g1 = [1, 2, 3]
        g2 = [4]
        gsp = self.config_content_dict["game_downloaded_path"]
        if int(self.config_content_dict["org_gsini"]) in g1:
            org_f = "YuanShen"
            zip_f = "GenshinImpact"
            zip_m = "i"
        else:
            org_f = "GenshinImpact"
            zip_f = "YuanShen"
            zip_m = "c"
        rename(gsp + "/" + org_f + "_Data", gsp + "/" + zip_f + "_Data")
        for i in file_paths:
            if self.sources_path_in_zip != "":
                isp = i.split(self.sources_path_in_zip)[-1]
            else:
                isp = i
            if isp[-13:] == "PCGameSDK.dll":
                pass
            else:
                copy("custom_launcher_sources\\icchange\\"+i,gsp + "/" + isp + ".backup" + zip_m)
        rename(gsp + "/" + zip_f + "_Data", gsp + "/" + org_f + "_Data")

    def c_s(self,tar_idx):
        res=False
        g1=[1,2,3]
        g2=[4]
        gsp=self.config_content_dict["game_downloaded_path"]
        if int(self.config_content_dict["org_gsini"]) in g1:
            org_s="c"
            zip_f="GenshinImpact"
        else:
            org_s="i"
            zip_f="YuanShen"
        if int(self.config_content_dict["now_mode"]) == 0:
            nd = int(self.config_content_dict["org_gsini"])
        else:
            nd = int(self.config_content_dict["now_mode"])
        if nd in g1:
            now_s="c"
        else:
            now_s="i"
        if int(tar_idx) in g1:
            tar_s="c"
        else:
            tar_s="i"
        if now_s==tar_s:
            res=True
        else:
            with open("custom_launcher_sources\\zpfps") as f:
                zpfps=f.read()
            file_paths=zpfps.split("\n")
            for i in listdir(gsp):
                if i[-5:]=="_Data":
                    now_sf=i.split("_Data")[0]
                    break
            if now_sf != zip_f:
                rename(gsp + "/" + now_sf + "_Data", gsp + "/" + zip_f + "_Data")
                fnc=True
            else:
                fnc=False
            if tar_s=="i":
                #rename(gsp+"/YuanShen.exe",gsp+"/YuanShen.exe"+".backup"+now_s)
                #tar_sf="GenshinImpact"
                if path.exists(gsp + "/" + zip_f + "_Data/Plugins/PCGameSDK.dll"):
                    rename(gsp+"/"+zip_f+"_Data/Plugins/PCGameSDK.dll",gsp+"/"+zip_f+"_Data/Plugins/PCGameSDK.dll.backupc")
                wf=""
                for i in file_paths:
                    if i!="":
                        try:
                            if self.sources_path_in_zip!="":
                                isp=i.split(self.sources_path_in_zip)[-1]
                            else:
                                isp=i
                            if isp==zip_f+".exe":
                                rename(gsp+"/YuanShen.exe",gsp+"/YuanShen.exe.backupc")
                                rename(gsp+"/GenshinImpact.exe.backupi",gsp+"/GenshinImpact.exe")
                            elif isp[-13:]=="PCGameSDK.dll":
                                pass
                            else:
                                rename(gsp+"/"+isp,gsp+"/"+isp+".backupc")
                                rename(gsp + "/" + isp+".backupi", gsp + "/" + isp)
                        except:
                            wf+=i+"\n"
                if wf!="":
                    print(wf)
                    QMessageBox().warning(self,"警告","以下文件在转换时出现错误：\n"+wf)
                    QMessageBox().information(self,"注意","请寻找技术支持，或前往原神启动器校验并修复文件（不推荐）")
                if fnc==False:
                    rename(gsp+"/"+"YuanShen_Data",gsp+"/"+"GenshinImpact_Data")
            else:
                if path.exists(gsp + "/" + zip_f + "_Data/Plugins/PCGameSDK.dll.backupc"):
                    rename(gsp + "/" + zip_f + "_Data/Plugins/PCGameSDK.dll.backupc",
                           gsp + "/" + zip_f + "_Data/Plugins/PCGameSDK.dll")
                wf=""
                for i in file_paths:
                    if i!="":
                        try:
                            if self.sources_path_in_zip!="":
                                isp=i.split(self.sources_path_in_zip)[-1]
                            else:
                                isp=i
                            if isp == zip_f + ".exe":
                                rename(gsp + "/GenshinImpact.exe", gsp + "/GenshinImpact.exe.backupi")
                                rename(gsp + "/YuanShen.exe.backupc", gsp + "/YuanShen.exe")
                            elif isp[-13:] == "PCGameSDK.dll":
                                pass
                            else:
                                rename(gsp + "/" + isp, gsp + "/" + isp + ".backupi")
                                rename(gsp + "/" + isp + ".backupc", gsp + "/" + isp)
                        except:
                            wf+=i+"\n"
                if wf!="":
                    print(wf)
                    QMessageBox().warning(self,"警告","以下文件在转换时出现错误：\n"+wf)
                    QMessageBox().information(self,"注意","请寻找技术支持，或前往原神启动器校验并修复文件（不推荐）")
                if fnc == False:
                    rename(gsp + "/" + "GenshinImpact_Data", gsp + "/" + "YuanShen_Data")
            res=True
        #print(res)
        return res

    def proc_exist(self,process_name):
        is_exist = False
        # wmi = win32com.client.GetObject('winmgmts:')
        # processCodeCov = wmi.ExecQuery('select * from Win32_Process where name=\"%s\"' % (process_name))
        # if len(processCodeCov) > 0:
        #     is_exist = True
        pl = pids()
        for pid in pl:
            if Process(pid).name() == process_name:
                is_exist=True
        return is_exist

    def start_url(self,url):
        webbrowser.open(url, new=0, autoraise=True)
        # webbrowser.open_new(url)
        # webbrowser.open_new_tab(url)

    def scfile_show(self,scfile_exist):
        if scfile_exist:
            startfile(f"{self.config_content_dict['game_downloaded_path']}/ScreenShot")

    def check_scfile(self,game_path):
        result=False
        if game_path!="":
            if path.exists(f'{self.config_content_dict["game_downloaded_path"]}/ScreenShot'):
                if listdir(f'{self.config_content_dict["game_downloaded_path"]}/ScreenShot'):
                    for i in listdir(f'{self.config_content_dict["game_downloaded_path"]}/ScreenShot'):
                        if i.split(".")[-1]=="png":
                            result=True
                            break
                        else:
                            pass
        return result
    def show_background(self,file_path:str):
        self.bgp_timer.stop()
        log_output={"error":False}
        try:
            file_type=path.splitext(file_path)[1]
            if file_type==".png" or file_type==".jpg" or file_type==".jpeg" or file_type==".jpe" or file_type==".jfif":
                self.background_img=QPixmap(file_path)
                self.bgp_show.setPixmap(self.background_img)
            elif file_type==".gif":
                self.background_img=QMovie(file_path)
                #self.background_img.loopCount(-1)
                self.bgp_show.setMovie(self.background_img)
                self.background_img.start()
            # elif file_type==".mp4":
            #     self.background_img=VideoCapture(file_path)
            #     #self.background_img_count=0
            #     self.background_img_count_max=self.background_img.get(CAP_PROP_FRAME_COUNT)
            #     self.bgp_timer.timeout.connect(self.show_background_mp4)
            #     self.bgp_timer.start(1000//int(self.background_img.get(CAP_PROP_FPS)))
            else:
                log_output["error"]=True
        except:
            log_output["error"]=True
        return log_output

    def bwiki_show(self):
        hg=[self.start_launcher,self.start_game,self.mode_set,self.modesel]
        if self.eventtype_bwiki_webview==True:
            self.verticalLayoutWidget.setEnabled(False)
            self.verticalLayoutWidget.setVisible(False)
            # for i in hg:
            #     i.setVisible(True)
            #     i.setEnabled(True)
            self.modesel.setVisible(True)
            self.modesel.setEnabled(True)
            self.modesel_event()
            self.eventtype_bwiki_webview=False
        else:
            for i in hg:
                i.setEnabled(False)
                i.setVisible(False)
            self.verticalLayoutWidget.setVisible(True)
            self.verticalLayoutWidget.setEnabled(True)
            self.eventtype_bwiki_webview=True


    # def show_background_mp4(self):
    #     if self.background_img_count<=self.background_img_count_max:
    #         r,f=self.background_img.read()
    #         self.background_img_count+=1
    #         f1=cvtColor(f,COLOR_BGR2RGB)
    #         f2=QImage(f1.data, f1.shape[1], f1.shape[0], f1.shape[1] * f1.shape[2],QImage.Format_RGB888)
    #         self.bgp_show.setPixmap(QPixmap.fromImage(f2))
    #     else:
    #         self.background_img_count=0
    #         self.background_img.set(CAP_PROP_POS_FRAMES,self.background_img_count)

    # def show_background_mp4(self):
    #     #environ["CUDA_VISIBLE_DEVICES"] = "1"
    #     r,f=self.background_img.read()
    #     if r:
    #         f1=cvtColor(f,COLOR_BGR2RGB)
    #         f2=QImage(f1.data, f1.shape[1], f1.shape[0], f1.shape[1] * f1.shape[2],QImage.Format_RGB888)
    #         self.bgp_show.setPixmap(QPixmap.fromImage(f2))
    #     else:
    #         self.background_img.set(CAP_PROP_POS_FRAMES,0)



    # def mousePosDetect_count_1(self):
    #     self.mousePosDetect()
    #     QTimer().singleShot(1,self.mousePosDetect_count_2)
    # def mousePosDetect_count_2(self):
    #     self.mousePosDetect()
    #     QTimer().singleShot(1,self.mousePosDetect_count_1)
    # def mousePosDetect(self):
    #     x=QCursor.pos().x()
    #     y=QCursor.pos().y()
    #     #self.setMouseTracking(True)
    #     #print(x,y)
    #     if 0<=y<=41:
    #         if 1245<=x<=1281:
    #             self.win_con.setPixmap(QPixmap("custom_launcher_sources\\win_title_exit.png"))
    #         elif 1206<=x<=1244:
    #             self.win_con.setPixmap(QPixmap("custom_launcher_sources\\win_title_mini.png"))
    #         elif 1172<=x<=1201:
    #             self.win_con.setPixmap(QPixmap("custom_launcher_sources\\win_title_setting.png"))
    #         else:
    #             self.win_con.setPixmap(QPixmap("custom_launcher_sources\\win_title.png"))
    #     else:
    #         self.win_con.setPixmap(QPixmap("custom_launcher_sources\\win_title.png"))
    def mouseMoveEvent(self, event):
        pass_accept=True
        x=event.pos().x()
        y=event.pos().y()
        #self.setMouseTracking(True)
        #print(x,y)
        # print(self.settingsel_path_bgp_selbt.x(),self.settingsel_path_bgp_selbt.y(),self.settingsel_path_bgp_selbt.x()+self.settingsel_path_bgp_selbt.width(),self.settingsel_path_bgp_selbt.y() + self.settingsel_path_bgp_selbt.height())
        # print(x-self.settings_group.x(),y-self.settings_group.y())
        if pass_accept==True:
            if self.eventtype_setting==False:
                if 0 <= y <= 41:
                    if 1245<=x<=1281 and self.eventtype_exitenable==True:
                        if self.scfile_exist:
                            self.win_con.setPixmap(QPixmap("custom_launcher_sources\\win_title_exit_scfile.png"))
                        else:
                            self.win_con.setPixmap(QPixmap("custom_launcher_sources\\win_title_exit.png"))
                    elif 1206<=x<=1244:
                        if self.scfile_exist:
                            self.win_con.setPixmap(QPixmap("custom_launcher_sources\\win_title_mini_scfile.png"))
                        else:
                            self.win_con.setPixmap(QPixmap("custom_launcher_sources\\win_title_mini.png"))
                    elif 1172<=x<=1201 and self.eventtype_allenable==True and self.eventtype_bwiki_webview==False:
                        if self.scfile_exist:
                            self.win_con.setPixmap(QPixmap("custom_launcher_sources\\win_title_setting_scfile.png"))
                        else:
                            self.win_con.setPixmap(QPixmap("custom_launcher_sources\\win_title_setting.png"))
                    elif 1130<=x<=1165:
                        if self.scfile_exist:
                            self.win_con.setPixmap(QPixmap("custom_launcher_sources\\win_title_scshot.png"))
                    else:
                        if self.scfile_exist:
                            self.win_con.setPixmap(QPixmap("custom_launcher_sources\\win_title_scfile.png"))
                        else:
                            self.win_con.setPixmap(QPixmap("custom_launcher_sources\\win_title.png"))
                    # if self.eventtype_leftmouse==True and x<1172:
                    #     #print("1")
                    #     self.move(event.globalPos()-self.win_p)#QCursor.pos().x()-x,QCursor.pos().y()-y)
                else:
                    if self.scfile_exist:
                        self.win_con.setPixmap(QPixmap("custom_launcher_sources\\win_title_scfile.png"))
                    else:
                        self.win_con.setPixmap(QPixmap("custom_launcher_sources\\win_title.png"))
                if self.mode_set.y()<=y<=self.mode_set.y()+self.mode_set.height():
                    if self.start_game.x()<=x<=self.start_game.x()+self.start_game.width() and self.eventtype_allenable==True and self.start_game.isVisible():
                        self.setCursor(Qt.PointingHandCursor)
                    # else:
                    #     self.setCursor(Qt.ArrowCursor)
                    elif self.detect_pos(x,y,self.mode_set,None)==True and self.eventtype_allenable==True and self.mode_set.isVisible():
                        self.setCursor(Qt.PointingHandCursor)
                    # else:
                    #     self.setCursor(Qt.ArrowCursor)
                    elif self.detect_pos(x,y,self.start_launcher,None)==True and self.start_launcher.isVisible():
                        self.setCursor(Qt.PointingHandCursor)
                    else:
                        self.setCursor(Qt.ArrowCursor)
                # else:
                #     self.setCursor(Qt.ArrowCursor)
                elif self.detect_pos(x,y,self.start_bwiki,None)==True and self.start_bwiki.isVisible():
                    self.setCursor(Qt.PointingHandCursor)
                else:
                    self.setCursor(Qt.ArrowCursor)
            elif self.eventtype_setting==True and self.eventtype_normal==False:
                if (self.setting_exit.y() + self.settings_group.y()) <= y <= (self.setting_exit.y() + self.settings_group.y() + self.setting_exit.height()) and (self.setting_exit.x()+self.settings_group.x()) <= x <= (self.setting_exit.x()+self.setting_exit.width()+self.settings_group.x()):
                    self.setting_exit.setPixmap(QPixmap("custom_launcher_sources\\setting_exit_touch.png"))
                else:
                    self.setting_exit.setPixmap(QPixmap("custom_launcher_sources\\setting_exit.png"))
                if (self.settingsel_path.y() + self.settings_group.y()) <= y <= (self.settingsel_path.y() + self.settings_group.y() + self.settingsel_path.height()) and (self.settingsel_path.x()+self.settings_group.x()) <= x <= (self.settingsel_path.x()+self.settingsel_path.width()+self.settings_group.x()):
                    self.settingsel_path.setPixmap(QPixmap("custom_launcher_sources\\settingsel_path_touch.png"))
                else:
                    if self.eventtype_setting_path==False:
                        self.settingsel_path.setPixmap(QPixmap("custom_launcher_sources\\settingsel_path.png"))
                if (self.settingsel_change2i.y()) <= y - self.settings_group.y() <= (self.settingsel_change2i.y() + self.settingsel_change2i.height()) and (self.settingsel_change2i.x()) <= x-self.settings_group.x() <= (self.settingsel_change2i.x()+self.settingsel_change2i.width()):
                    self.settingsel_change2i.setPixmap(QPixmap("custom_launcher_sources\\settingsel_change2i_touch.png"))
                else:
                    if self.eventtype_setting_change2i==False:
                        self.settingsel_change2i.setPixmap(QPixmap("custom_launcher_sources\\settingsel_change2i.png"))
                if self.eventtype_setting_path==True:
                    if self.settingsel_path_bgp_selbt.y() <= y-self.settings_group.y() <= (self.settingsel_path_bgp_selbt.y() + self.settingsel_path_bgp_selbt.height()) and self.settingsel_path_bgp_selbt.x() <= x-self.settings_group.x() <= (self.settingsel_path_bgp_selbt.x()+self.settingsel_path_bgp_selbt.width()):
                        self.settingsel_path_bgp_selbt.setPixmap(QPixmap("custom_launcher_sources\\settingsel_path_bgp_selbt_touch.png"))
                    else:
                        self.settingsel_path_bgp_selbt.setPixmap(QPixmap("custom_launcher_sources\\settingsel_path_bgp_selbt.png"))
                        #self.setting_exit.setPixmap(QPixmap("custom_launcher_sources\\setting_exit.png"))
                    if self.settingsel_path_gl_selbt.y() <= y-self.settings_group.y() <= (self.settingsel_path_gl_selbt.y() + self.settingsel_path_gl_selbt.height()) and self.settingsel_path_gl_selbt.x() <= x-self.settings_group.x() <= (self.settingsel_path_gl_selbt.x()+self.settingsel_path_gl_selbt.width()):
                        self.settingsel_path_gl_selbt.setPixmap(QPixmap("custom_launcher_sources\\settingsel_path_gl_selbt_touch.png"))
                    else:
                        self.settingsel_path_gl_selbt.setPixmap(QPixmap("custom_launcher_sources\\settingsel_path_gl_selbt.png"))
                    if self.settingsel_path_gs_selbt.y() <= y-self.settings_group.y() <= (self.settingsel_path_gs_selbt.y() + self.settingsel_path_gs_selbt.height()) and self.settingsel_path_gs_selbt.x() <= x-self.settings_group.x() <= (self.settingsel_path_gs_selbt.x()+self.settingsel_path_gs_selbt.width()):
                        self.settingsel_path_gs_selbt.setPixmap(QPixmap("custom_launcher_sources\\settingsel_path_gs_selbt_touch.png"))
                    else:
                        self.settingsel_path_gs_selbt.setPixmap(QPixmap("custom_launcher_sources\\settingsel_path_gs_selbt.png"))
                if self.eventtype_setting_change2i==True:
                    if self.settingsel_change2i_zip_selbt.y() <= y-self.settings_group.y() <= (self.settingsel_change2i_zip_selbt.y() + self.settingsel_change2i_zip_selbt.height()) and self.settingsel_change2i_zip_selbt.x() <= x-self.settings_group.x() <= (self.settingsel_change2i_zip_selbt.x()+self.settingsel_change2i_zip_selbt.width()):
                        self.settingsel_change2i_zip_selbt.setPixmap(QPixmap("custom_launcher_sources\\settingsel_change2i_zip_selbt_touch.png"))
                    else:
                        self.settingsel_change2i_zip_selbt.setPixmap(QPixmap("custom_launcher_sources\\settingsel_change2i_zip_selbt.png"))
                    if self.detect_pos(x,y,self.settingsel_change2i_article,self.settings_group)==True and self.settingsel_change2i_article.isVisible():
                        self.settingsel_change2i_article.setPixmap(QPixmap("custom_launcher_sources\\settingsel_change2i_article_touch.png"))
                    else:
                        self.settingsel_change2i_article.setPixmap(QPixmap("custom_launcher_sources\\settingsel_change2i_article.png"))
                    if self.detect_pos(x,y,self.settingsel_change2i_download,self.settings_group)==True and self.settingsel_change2i_download.isVisible():
                        self.settingsel_change2i_download.setPixmap(QPixmap("custom_launcher_sources\\settingsel_change2i_download_touch.png"))
                    else:
                        self.settingsel_change2i_download.setPixmap(QPixmap("custom_launcher_sources\\settingsel_change2i_download.png"))

            else:
                if self.scfile_exist:
                    self.win_con.setPixmap(QPixmap("custom_launcher_sources\\win_title_scfile.png"))
                else:
                    self.win_con.setPixmap(QPixmap("custom_launcher_sources\\win_title.png"))
                self.setting_exit.setPixmap(QPixmap("custom_launcher_sources\\setting_exit.png"))
        else:
            pass
        if 0 <= y <= 41:
            if self.eventtype_leftmouse == True and x < 1172:
                self.move(event.globalPos() - self.win_p)
            #pass

    def mousePressEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()
        # self.setMouseTracking(True)
        # print(x,y)
        if 0 <= y <= 41 and self.eventtype_setting == False:
            if self.scfile_exist:
                xl=1130
            else:
                xl=1172
            if event.button() == Qt.MouseButton.LeftButton and x < xl:
                self.eventtype_leftmouse=True
                self.win_p=event.globalPos()-self.pos()
                #print("1")
                #self.move(QCursor.pos().x() - x, QCursor.pos().y() - y)
    #     button=event.button()
    #     #print(button)
    #     if button==Qt.MouseButton.LeftButton:
    #         x=QCursor.pos().x()
    #         y=QCursor.pos().y()
    #         if 0 <= y <= 41:
    #             if 1172 > x:
    #                 self.move(x,y)

    def mouseReleaseEvent(self, event):
        pass_accept=True
        button = event.button()
        # print(button)
        if pass_accept==True:#self.eventtype_allenable==True:
            if button == Qt.MouseButton.LeftButton:
                self.eventtype_leftmouse=False
                x = event.pos().x()
                y = event.pos().y()
                if self.eventtype_setting==False:
                    if 0<=y<=41:
                        if 1245 <= x <= 1281 and self.eventtype_exitenable==True:
                            sys.exit()
                        elif 1206 <= x <= 1244:
                            self.showMinimized()
                        elif 1172 <= x <= 1201 and self.start_bwiki.isVisible() and self.eventtype_allenable==True and self.eventtype_bwiki_webview==False:
                            self.settings_show(True)
                        elif 1130 <= x <= 1165:
                            self.scfile_show(self.scfile_exist)
                    if self.mode_set.y() <= y <= self.mode_set.y() + self.mode_set.height():
                        if self.mode_set.x() <= x <= self.mode_set.x() + self.mode_set.width() and self.eventtype_allenable==True and self.mode_set.isVisible():
                            self.set_nowmode()
                        elif self.start_game.x()<=x<=self.start_game.x()+self.start_game.width() and self.eventtype_allenable==True and self.start_game.isVisible():
                            self.start_g()
                        elif self.start_launcher.x()<=x<=self.start_launcher.x()+self.start_launcher.width() and self.mode_set.isVisible() and self.start_launcher.isVisible():
                            self.start_gl()
                    if self.detect_pos(x, y, self.start_bwiki, None) == True and self.start_bwiki.isVisible():
                        self.bwiki_show()
                elif self.eventtype_setting==True and self.eventtype_normal==False:
                    if (self.setting_exit.y() + self.settings_group.y()) <= y <= (
                            self.setting_exit.y() + self.settings_group.y() + self.setting_exit.height()) and (
                            self.setting_exit.x() + self.settings_group.x()) <= x <= (
                            self.setting_exit.x() + self.setting_exit.width() + self.settings_group.x()):
                        self.settings_show(False)
                    if (self.settingsel_path.y() + self.settings_group.y()) <= y <= (
                            self.settingsel_path.y() + self.settings_group.y() + self.settingsel_path.height()) and (
                            self.settingsel_path.x() + self.settings_group.x()) <= x <= (
                            self.settingsel_path.x() + self.settingsel_path.width() + self.settings_group.x()):
                        self.settingsel_change2i_event(False)
                        self.settingsel_path_event(True)
                    if (self.settingsel_change2i.y()) <= y - self.settings_group.y() <= (
                            self.settingsel_change2i.y() + self.settingsel_change2i.height()) and (
                    self.settingsel_change2i.x()) <= x - self.settings_group.x() <= (
                            self.settingsel_change2i.x() + self.settingsel_change2i.width()):
                        self.settingsel_path_event(False)
                        self.settingsel_change2i_event(True)
                    if self.eventtype_setting_path==True:
                        if self.settingsel_path_bgp_selbt.y() <= y - self.settings_group.y() <= (
                                self.settingsel_path_bgp_selbt.y() + self.settingsel_path_bgp_selbt.height()) and self.settingsel_path_bgp_selbt.x() <= x - self.settings_group.x() <= (
                                self.settingsel_path_bgp_selbt.x() + self.settingsel_path_bgp_selbt.width()):
                            self.sel_bgp()
                        if self.settingsel_path_gl_selbt.y() <= y - self.settings_group.y() <= (
                                self.settingsel_path_gl_selbt.y() + self.settingsel_path_gl_selbt.height()) and self.settingsel_path_gl_selbt.x() <= x - self.settings_group.x() <= (
                                self.settingsel_path_gl_selbt.x() + self.settingsel_path_gl_selbt.width()) and self.settingsel_path_gl_selbt.isVisible():
                            self.sel_gl()
                        if self.settingsel_path_gs_selbt.y() <= y - self.settings_group.y() <= (
                                self.settingsel_path_gs_selbt.y() + self.settingsel_path_gs_selbt.height()) and self.settingsel_path_gs_selbt.x() <= x - self.settings_group.x() <= (
                                self.settingsel_path_gs_selbt.x() + self.settingsel_path_gs_selbt.width()) and self.settingsel_path_gs_selbt.isVisible():
                            self.sel_gs()
                    ########    转服资源    栏检测     ############
                    if self.detect_pos(x,y,self.settingsel_change2i_zip_selbt,self.settings_group)==True and self.settingsel_change2i_zip_selbt.isVisible():
                        self.sel_zip()
                    if self.detect_pos(x,y,self.settingsel_change2i_article,self.settings_group)==True and self.settingsel_change2i_article.isVisible():
                        self.start_url("https://www.bilibili.com/read/cv15768559")
                    if self.detect_pos(x,y,self.settingsel_change2i_download,self.settings_group)==True and self.settingsel_change2i_download.isVisible():
                        self.start_url("https://pan.baidu.com/s/1D-gEfE2QLV0fA4Ut3oVfiQ?pwd=yowv")
        else:
            if button==Qt.MouseButton.LeftButton:
                self.eventtype_leftmouse = False
                x = event.pos().x()
                y = event.pos().y()
                if 0 <= y <= 41 and x<1172:
                    pass
                else:
                    QMessageBox().warning(self,"注意","原神已启动，为避免程序或文件错误，该功能已禁用，以及请勿关闭启动器")
    def detect_pos(self,x,y,item,group):
        if group!=None:
            if item.y() <= y - group.y() <= (item.y() + item.height()) and item.x() <= x - group.x() <= (item.x() + item.width()):
                res=True
            else:
                res=False
        else:
            if item.y() <= y <= (item.y() + item.height()) and item.x() <= x <= (item.x() + item.width()):
                res=True
            else:
                res=False
        return res
    def detect_launched_1(self):
        if self.proc_exist("YuanShen.exe")==True or self.proc_exist("GenshinImpact.exe")==True:
            self.eventtype_allenable=False
            self.eventtype_exitenable=False
        else:
            self.eventtype_allenable=True
            self.eventtype_exitenable=True
        try:
            self.scfile_exist = self.check_scfile(self.config_content_dict["game_downloaded_path"])
        except:
            self.scfile_exist=False
        #QTimer().singleShot(500,self.detect_launched_2)
    # def detect_launched_2(self):
    #     if self.proc_exist("YuanShen.exe")==True or self.proc_exist("GenshinImpact.exe")==True:
    #         self.eventtype_allenable=False
    #         self.eventtype_exitenable = False
    #     else:
    #         self.eventtype_allenable=True
    #         self.eventtype_exitenable = True
    #     try:
    #         self.scfile_exist = self.check_scfile(self.config_content_dict["game_downloaded_path"])
    #     except:
    #         self.scfile_exist = False
    #     QTimer().singleShot(500,self.detect_launched_1)

if __name__=="__main__":
    app=QApplication(sys.argv)
    myappid = 'mycompany.myproduct.subproduct.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    app.setWindowIcon(QIcon("custom_launcher_sources\\app.png"))
    wi=mainwin()
    sys.exit(app.exec_())
