from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap, QPainter, QColor, QPaintEvent, QMouseEvent, QPen, QCursor
from PySide6.QtCore import Qt, QSize


class PainterWidget(QWidget):

    def __init__(self, size: QSize, parent=None):
        super().__init__(parent)
        self.setFixedSize(size)
        self._pixmap = QPixmap(size)
        self._pixmap.fill(QColor('white'))

        self._previous_pos = None
        self._painter = QPainter()
        self._pen = QPen()
        self._pen.setCapStyle(Qt.RoundCap)
        self._pen.setJoinStyle(Qt.RoundJoin)
        self.setCursor(Qt.CursorShape.CrossCursor)

    def set_pen_width(self, value: float):
        """ Setting pen width """
        self._pen.setWidthF(value)

    def set_pen_color(self, color):
        """ Setting the pen color """
        self._pen.setColor(color)

    def set_size(self, size: QSize):
        self.resize(size)
        self.update()

    def paintEvent(self, event: QPaintEvent):
        """ Paint the Pixmap into the widget """
        with QPainter(self) as painter:
            painter.drawPixmap(0, 0, self._pixmap)

    def mousePressEvent(self, event: QMouseEvent):
        """ Called when user clicks on the mouse """
        self._previous_pos = event.position().toPoint()
        QWidget.mousePressEvent(self, event)

    def mouseMoveEvent(self, event: QMouseEvent):
        """ Called when user moves and clicks on the mouse """
        current_pos = event.position().toPoint()
        self._painter.begin(self._pixmap)
        self._painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        self._painter.setPen(self._pen)
        self._painter.drawLine(self._previous_pos, current_pos)
        self._painter.end()

        self._previous_pos = current_pos
        self.update()

        QWidget.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        """ Called when user releases the mouse """
        self._previous_pos = None
        QWidget.mouseReleaseEvent(self, event)

    def save(self, filename: str):
        """ Save pixmap to filename """
        self._pixmap.save(filename)

    def load(self, filename: str):
        """ Load pixmap from filename """
        self._pixmap.load(filename)
        """ 
            The recommended minimum window width is 250 px, since there are buttons in the panel.
        """
        if self._pixmap.size().width() > QSize(250, 250).width():
            # If the size of the uploaded image is larger than the specified minimum
            self._pixmap = self._pixmap.scaled(self._pixmap.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        else:
            # Otherwise stretch the image
            self._pixmap = self._pixmap.scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatio)

        self.update()

        # Resize widget
        self.setFixedSize(self._pixmap.size())

    def clear(self):
        """ Clear the pixmap """
        self._pixmap.fill(QColor('white'))
        self.update()