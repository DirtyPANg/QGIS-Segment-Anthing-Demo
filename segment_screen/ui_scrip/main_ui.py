from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget, QDialog
from .all_mode_ui import Ui_SegmentScreenDialogBase
from .setting_ui import Ui_SettingsDialog
import sys

class MainUi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Segment Anything")

        widget = QWidget(self)
        self.setCentralWidget(widget)

        # 主布局是垂直布局
        main_layout = QVBoxLayout()
        widget.setLayout(main_layout)

        # 按钮放在一个水平布局中
        button_layout = QHBoxLayout()

        # 创建四个按钮
        self.btn_all_segment_mode = QPushButton('All Segment Mode')
        self.btn_prompt_mode = QPushButton('Prompt Mode')
        self.btn_picking_mode = QPushButton('Picking Mode')
        self.btn_setting = QPushButton('Setting')

        # 把按钮添加到水平布局中
        button_layout.addWidget(self.btn_all_segment_mode)
        button_layout.addWidget(self.btn_prompt_mode)
        button_layout.addWidget(self.btn_picking_mode)
        button_layout.addWidget(self.btn_setting)

        # 把水平布局添加到主布局的最上面
        main_layout.addLayout(button_layout)

        # 创建一个QStackedWidget，把各个模式的界面添加到其中
        self.stacked_widget = QStackedWidget()
        main_layout.addWidget(self.stacked_widget)

        self.all_mode_dialog = QDialog()
        self.all_mode_ui = Ui_SegmentScreenDialogBase()
        self.all_mode_ui.setupUi(self.all_mode_dialog)
        self.stacked_widget.addWidget(self.all_mode_dialog)

        self.setting_dialog = QDialog()
        self.setting_ui = Ui_SettingsDialog()
        self.setting_ui.setupUi(self.setting_dialog)
        self.stacked_widget.addWidget(self.setting_dialog)

        # 为按钮添加点击事件
        self.btn_all_segment_mode.clicked.connect(self.show_all_segment_mode)
        self.btn_prompt_mode.clicked.connect(self.show_prompt_mode)
        self.btn_picking_mode.clicked.connect(self.show_picking_mode)
        self.btn_setting.clicked.connect(self.show_setting)

        # 默认显示 All Segment Mode 界面
        self.show_all_segment_mode()

    # 下面是按钮点击事件对应的方法，你可以在这里切换到对应的模式界面
    def show_all_segment_mode(self):
        self.stacked_widget.setCurrentWidget(self.all_mode_dialog)

    def show_prompt_mode(self):
        print('Prompt Mode')

    def show_picking_mode(self):
        print('Picking Mode')

    def show_setting(self):
        self.stacked_widget.setCurrentWidget(self.setting_dialog)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_ui = MainUi()
    main_ui.show()

    sys.exit(app.exec_())
