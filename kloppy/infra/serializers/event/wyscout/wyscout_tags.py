from enum import Enum

GOAL = 101
OWN_GOAL = 102

OPPORTUNITY = 201

ASSIST = 301
KEY_PASS = 302

LEFT_FOOT = 401
RIGHT_FOOT = 402
HEAD_BODY = 403

FREE_SPACE_RIGHT = 501
FREE_SPACE_LEFT = 502
FREE_SPACE_ON_LEFT = 503
FREE_SPACE_ON_RIGHT = 504

ANTICIPATED = 601
ANTICIPATION = 602

LOST = 701
NEUTRAL = 702
WON = 703

HIGH = 801
LOW = 802

THROUGH = 901

FAIRPLAY = 1001

DIRECT = 1101
INDIRECT = 1102

FEINT = 1301
MISSED_BALL = 1302

GOAL_LOW_CENTER = 1201
GOAL_LOW_RIGHT = 1202
GOAL_CENTER = 1203
GOAL_CENTER_LEFT = 1204
GOAL_LOW_LEFT = 1205
GOAL_CENTER_RIGHT = 1206
GOAL_HIGH_CENTER = 1207
GOAL_HIGH_LEFT = 1208
GOAL_HIGH_RIGHT = 1209

SHOT_ON_GOAL = list(range(1201, 1209 + 1))

OUT_LOW_RIGHT = 1210
OUT_CENTER_LEFT = 1211
OUT_LOW_LEFT = 1212
OUT_CENTER_RIGHT = 1213
OUT_HIGH_CENTER = 1214
OUT_HIGH_LEFT = 1215
OUT_HIGH_RIGHT = 1216

SHOT_OFF_TARGET = list(range(1210, 1216 + 1))

POST_LOW_RIGHT = 1217
POST_CENTER_LEFT = 1218
POST_LOW_LEFT = 1219
POST_CENTER_RIGHT = 1220
POST_HIGH_CENTER = 1221
POST_HIGH_LEFT = 1222
POST_HIGH_RIGHT = 1223

SHOT_POST = list(range(1217, 1223 + 1))

INTERCEPTION = 1401

CLEARANCE = 1501

SLIDING_TACKLE = 1601

RED_CARD = 1701
YELLOW_CARD = 1702
SECOND_YELLOW_CARD = 1703

CARD = list(range(1701, 1703 + 1))

ACCURATE = 1801
NOT_ACCURATE = 1802

COUNTER_ATTACK = 1901

DANGEROUS_BALL_LOST = 2001

BLOCKED = 2101


class ShotZoneResults(Enum):
    GoalBottomLeft = "glb"
    GoalBottomRight = "gbr"
    GoalBottomCenter = "gbc"
    GoalCenterLeft = "gcl"
    GoalCenter = "gc"
    GoalCenterRight = "gcr"
    GoalTopLeft = "gtl"
    GoalTopRight = "gtr"
    GoalTopCenter = "gtc"
    OutBottomRight = "obr"
    OutBottomLeft = "obl"
    OutRight = "or"
    OutLeft = "ol"
    OutLeftTop = "olt"
    OutTop = "ot"
    OutRightTop = "ort"
    Blocked = "bc"
