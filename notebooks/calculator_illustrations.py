
from jp_doodle.dual_canvas import swatch
from jp_doodle.auto_capture import embed_hidden
import inspect

DO_EMBEDDINGS = False

def final_fit(frame, file_prefix=None):
    if DO_EMBEDDINGS:
        if file_prefix is None:
            file_prefix = inspect.stack()[1][3]
        filename = file_prefix + ".png"
        canvas_widget = frame.get_canvas()
        with embed_hidden(canvas_widget, filename):
            frame.fit()
    else:
        frame.fit()

def rect_34_22():
    s = swatch(model_height=34, pixels=200)
    s.frame_rect(0, 0, 34, 22, color="#999")
    s.text(17, 23, "width=34", align="center")
    s.text(35, 11, "height=22", degrees="-90", align="center")
    s.text
    final_fit(s)

def triangle_34_22():
    s = swatch(model_height=34, pixels=200)
    s.polygon([(-10, 0), (24, 0), (0, 22)], color="#999")
    s.text(5, -2, "width=34", align="center")
    s.text(1, 11, "height=22", degrees="-90", align="center")
    s.line(0, 1, 0, 21)
    s.text
    final_fit(s)

p1 = (5, 2)
p2 = (13, 21)
p3 = (22, 7)

def triangle_coords():
    s = swatch(model_height=34, pixels=200)
    coords = [p1, p2, p3]
    s.polygon(coords, color="#999")
    for (nm, p, align) in [("p1", p1, "right"), ("p2", p2, "center"), ("p3", p3, "left")]:
        (x,y) = p
        s.text(x,y, nm+"="+repr(p), align=align)
    s.fit()
    s.lower_left_axes(min_x=0, max_x=22, min_y=0, max_tick_count=2)
    final_fit(s)

def quad(s, p1, p2, color, fill=True, outlinecolor=None):
    p3 = list(p2)
    p3[1] = 0
    p4 = list(p1)
    p4[1] = 0
    s.polygon([p1, p2, p3, p4], color=color, fill=fill, lineWidth=4)
    if outlinecolor:
        s.polygon([p1, p2, p3, p4], color=outlinecolor, fill=fill, lineWidth=4)

def triangle_subproblems():
    s = swatch(model_height=34, pixels=200)
    coords = [p1, p2, p3]
    s.polygon(coords, color="#999")
    for (p, align) in [(p1, "right"), (p2, "center"), (p3, "left")]:
        (x,y) = p
        s.text(x,y, repr(p), align=align)
    quad(s, p1, p2, color="rgba(255, 100, 100, 0.3)")
    quad(s, p2, p3, color="rgba(100, 255, 100, 0.3)")
    quad(s, p1, p3, color="rgba(100, 100, 255, 0.3)", fill=False, outlinecolor="rgba(100, 100, 255, 1)")
    s.fit()
    s.lower_left_axes(min_x=0, max_x=22, min_y=0, max_tick_count=2)
    final_fit(s)

def abstract_quad():
    s = swatch(model_height=34, pixels=200)
    for (p, align, txt) in [(p2, "right", "(x1,y1)"), (p3, "left", "(x2,y2)")]:
        (x,y) = p
        s.text(x,y, txt, align=align)
    quad(s, p2, p3, color="rgba(100, 255, 100, 1)")
    s.fit()
    s.lower_left_axes(min_x=0, max_x=22, min_y=0, max_tick_count=2)
    final_fit(s)
