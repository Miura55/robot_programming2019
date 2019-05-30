import cv2

tgt = cv2.imread("model_2.png", cv2.IMREAD_COLOR)
sz = tgt.shape
moz = cv2.resize(cv2.resize(tgt, (sz[1]//10, sz[0]//10)), (sz[1], sz[0]))
sch = cv2.imread("search.png", cv2.IMREAD_COLOR)
(minv, maxv, minl, maxl) = cv2.minMaxLoc(cv2.matchTemplate(tgt, sch,
cv2.TM_CCOEFF_NORMED))
if (maxv > 0.9) :
    (h, w, ch) = sch.shape
    tgt[maxl[1]:maxl[1] + h, maxl[0]: maxl[0] + w] = moz[maxl[1]:maxl[1] + h,
    maxl[0]: maxl[0] + w]
cv2.imwrite("result.png", tgt)
