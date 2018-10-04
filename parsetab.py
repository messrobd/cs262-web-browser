
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'jsleftORORleftANDANDleftEQUALEQUALleftLTGTLEGEleftPLUSMINUSleftTIMESDIVIDEMODULOrightNOTANDAND COMMA DIVIDE ELSE EQUAL EQUALEQUAL FALSE FUNCTION GE GT IDENTIFIER IF LBRACE LE LPAREN LT MINUS MODULO NOT NUMBER OROR PLUS RBRACE RETURN RPAREN SEMICOLON STRING TIMES TRUE VARjs : element jsjs : element : FUNCTION IDENTIFIER LPAREN optparams RPAREN compoundstmtelement : stmt SEMICOLONoptparams : paramsoptparams : params : IDENTIFIER COMMA paramsparams : IDENTIFIERcompoundstmt : LBRACE statements RBRACEstatements : stmt SEMICOLON statementsstatements : stmt : IF exp compoundstmtstmt : IF exp compoundstmt ELSE compoundstmtstmt : IDENTIFIER EQUAL expstmt : RETURN expstmt : VAR IDENTIFIER EQUAL expstmt : VAR IDENTIFIER EQUAL FUNCTION LPAREN optparams RPAREN compoundstmtstmt : expexp : NOT expexp : LPAREN exp RPARENexp : exp OROR exp\n            | exp ANDAND exp\n            | exp EQUALEQUAL exp\n            | exp LT exp\n            | exp GT exp\n            | exp LE exp\n            | exp GE exp\n            | exp PLUS exp\n            | exp MINUS exp\n            | exp TIMES exp\n            | exp DIVIDE exp\n            | exp MODULO exp exp : IDENTIFIER LPAREN optargs RPARENoptargs : argsoptargs : args : exp COMMA argsargs : expexp : IDENTIFIERexp : NUMBERexp : STRINGexp : TRUEexp : FALSE'
    
_lr_action_items = {'OROR':([2,3,4,6,12,14,16,17,22,24,38,39,42,44,48,49,50,51,52,53,54,55,56,57,58,59,60,66,],[-40,-41,-38,-39,-42,26,-38,26,26,26,-19,26,26,-20,-21,-22,-25,-32,-31,-27,-30,-24,-26,-28,-23,-29,-33,26,]),'RETURN':([0,13,21,46,74,75,78,],[1,1,-4,1,-9,1,-3,]),'NUMBER':([0,1,9,11,13,15,18,19,21,26,27,28,29,30,31,32,33,34,35,36,37,45,46,61,74,75,78,],[6,6,6,6,6,6,6,6,-4,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,-9,6,-3,]),'TRUE':([0,1,9,11,13,15,18,19,21,26,27,28,29,30,31,32,33,34,35,36,37,45,46,61,74,75,78,],[3,3,3,3,3,3,3,3,-4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,-9,3,-3,]),'MINUS':([2,3,4,6,12,14,16,17,22,24,38,39,42,44,48,49,50,51,52,53,54,55,56,57,58,59,60,66,],[-40,-41,-38,-39,-42,37,-38,37,37,37,-19,37,37,-20,37,37,37,-32,-31,37,-30,37,37,-28,37,-29,-33,37,]),'STRING':([0,1,9,11,13,15,18,19,21,26,27,28,29,30,31,32,33,34,35,36,37,45,46,61,74,75,78,],[2,2,2,2,2,2,2,2,-4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,-9,2,-3,]),'LE':([2,3,4,6,12,14,16,17,22,24,38,39,42,44,48,49,50,51,52,53,54,55,56,57,58,59,60,66,],[-40,-41,-38,-39,-42,34,-38,34,34,34,-19,34,34,-20,34,34,-25,-32,-31,-27,-30,-24,-26,-28,34,-29,-33,34,]),'RPAREN':([2,3,6,12,16,19,22,38,40,41,42,43,44,48,49,50,51,52,53,54,55,56,57,58,59,60,62,63,64,70,73,77,79,],[-40,-41,-39,-42,-38,-35,44,-19,-34,60,-37,-6,-20,-21,-22,-25,-32,-31,-27,-30,-24,-26,-28,-23,-29,-33,-5,-8,72,-36,-6,-7,81,]),'SEMICOLON':([2,3,4,6,7,12,14,16,17,38,39,44,47,48,49,50,51,52,53,54,55,56,57,58,59,60,66,68,74,76,82,],[-40,-41,-38,-39,21,-42,-18,-38,-15,-19,-14,-20,-12,-21,-22,-25,-32,-31,-27,-30,-24,-26,-28,-23,-29,-33,-16,75,-9,-13,-17,]),'LT':([2,3,4,6,12,14,16,17,22,24,38,39,42,44,48,49,50,51,52,53,54,55,56,57,58,59,60,66,],[-40,-41,-38,-39,-42,33,-38,33,33,33,-19,33,33,-20,33,33,-25,-32,-31,-27,-30,-24,-26,-28,33,-29,-33,33,]),'PLUS':([2,3,4,6,12,14,16,17,22,24,38,39,42,44,48,49,50,51,52,53,54,55,56,57,58,59,60,66,],[-40,-41,-38,-39,-42,35,-38,35,35,35,-19,35,35,-20,35,35,35,-32,-31,35,-30,35,35,-28,35,-29,-33,35,]),'COMMA':([2,3,6,12,16,38,42,44,48,49,50,51,52,53,54,55,56,57,58,59,60,63,],[-40,-41,-39,-42,-38,-19,61,-20,-21,-22,-25,-32,-31,-27,-30,-24,-26,-28,-23,-29,-33,71,]),'EQUALEQUAL':([2,3,4,6,12,14,16,17,22,24,38,39,42,44,48,49,50,51,52,53,54,55,56,57,58,59,60,66,],[-40,-41,-38,-39,-42,36,-38,36,36,36,-19,36,36,-20,36,36,-25,-32,-31,-27,-30,-24,-26,-28,-23,-29,-33,36,]),'IDENTIFIER':([0,1,5,9,10,11,13,15,18,19,21,26,27,28,29,30,31,32,33,34,35,36,37,43,45,46,61,71,73,74,75,78,],[4,16,20,16,23,16,4,16,16,16,-4,16,16,16,16,16,16,16,16,16,16,16,16,63,16,4,16,63,63,-9,4,-3,]),'$end':([0,8,13,21,25,74,78,],[-2,0,-2,-4,-1,-9,-3,]),'FUNCTION':([0,13,21,45,74,78,],[5,5,-4,65,-9,-3,]),'GT':([2,3,4,6,12,14,16,17,22,24,38,39,42,44,48,49,50,51,52,53,54,55,56,57,58,59,60,66,],[-40,-41,-38,-39,-42,28,-38,28,28,28,-19,28,28,-20,28,28,-25,-32,-31,-27,-30,-24,-26,-28,28,-29,-33,28,]),'MODULO':([2,3,4,6,12,14,16,17,22,24,38,39,42,44,48,49,50,51,52,53,54,55,56,57,58,59,60,66,],[-40,-41,-38,-39,-42,29,-38,29,29,29,-19,29,29,-20,29,29,29,-32,-31,29,-30,29,29,29,29,29,-33,29,]),'DIVIDE':([2,3,4,6,12,14,16,17,22,24,38,39,42,44,48,49,50,51,52,53,54,55,56,57,58,59,60,66,],[-40,-41,-38,-39,-42,30,-38,30,30,30,-19,30,30,-20,30,30,30,-32,-31,30,-30,30,30,30,30,30,-33,30,]),'EQUAL':([4,23,],[18,45,]),'RBRACE':([46,67,75,80,],[-11,74,-11,-10,]),'TIMES':([2,3,4,6,12,14,16,17,22,24,38,39,42,44,48,49,50,51,52,53,54,55,56,57,58,59,60,66,],[-40,-41,-38,-39,-42,32,-38,32,32,32,-19,32,32,-20,32,32,32,-32,-31,32,-30,32,32,32,32,32,-33,32,]),'GE':([2,3,4,6,12,14,16,17,22,24,38,39,42,44,48,49,50,51,52,53,54,55,56,57,58,59,60,66,],[-40,-41,-38,-39,-42,31,-38,31,31,31,-19,31,31,-20,31,31,-25,-32,-31,-27,-30,-24,-26,-28,31,-29,-33,31,]),'LPAREN':([0,1,4,9,11,13,15,16,18,19,20,21,26,27,28,29,30,31,32,33,34,35,36,37,45,46,61,65,74,75,78,],[9,9,19,9,9,9,9,19,9,9,43,-4,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,73,-9,9,-3,]),'VAR':([0,13,21,46,74,75,78,],[10,10,-4,10,-9,10,-3,]),'ELSE':([47,74,],[69,-9,]),'IF':([0,13,21,46,74,75,78,],[11,11,-4,11,-9,11,-3,]),'ANDAND':([2,3,4,6,12,14,16,17,22,24,38,39,42,44,48,49,50,51,52,53,54,55,56,57,58,59,60,66,],[-40,-41,-38,-39,-42,27,-38,27,27,27,-19,27,27,-20,27,-22,-25,-32,-31,-27,-30,-24,-26,-28,-23,-29,-33,27,]),'LBRACE':([2,3,6,12,16,24,38,44,48,49,50,51,52,53,54,55,56,57,58,59,60,69,72,81,],[-40,-41,-39,-42,-38,46,-19,-20,-21,-22,-25,-32,-31,-27,-30,-24,-26,-28,-23,-29,-33,46,46,46,]),'FALSE':([0,1,9,11,13,15,18,19,21,26,27,28,29,30,31,32,33,34,35,36,37,45,46,61,74,75,78,],[12,12,12,12,12,12,12,12,-4,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,-9,12,-3,]),'NOT':([0,1,9,11,13,15,18,19,21,26,27,28,29,30,31,32,33,34,35,36,37,45,46,61,74,75,78,],[15,15,15,15,15,15,15,15,-4,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,-9,15,-3,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statements':([46,75,],[67,80,]),'args':([19,61,],[40,70,]),'stmt':([0,13,46,75,],[7,7,68,68,]),'element':([0,13,],[13,13,]),'params':([43,71,73,],[62,77,62,]),'exp':([0,1,9,11,13,15,18,19,26,27,28,29,30,31,32,33,34,35,36,37,45,46,61,75,],[14,17,22,24,14,38,39,42,48,49,50,51,52,53,54,55,56,57,58,59,66,14,42,14,]),'js':([0,13,],[8,25,]),'optparams':([43,73,],[64,79,]),'compoundstmt':([24,69,72,81,],[47,76,78,82,]),'optargs':([19,],[41,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> js","S'",1,None,None,None),
  ('js -> element js','js',2,'p_js','js_parser.py',46),
  ('js -> <empty>','js',0,'p_js_empty','js_parser.py',50),
  ('element -> FUNCTION IDENTIFIER LPAREN optparams RPAREN compoundstmt','element',6,'p_element_func','js_parser.py',55),
  ('element -> stmt SEMICOLON','element',2,'p_element_stmt','js_parser.py',60),
  ('optparams -> params','optparams',1,'p_optparams','js_parser.py',64),
  ('optparams -> <empty>','optparams',0,'p_optparams_empty','js_parser.py',68),
  ('params -> IDENTIFIER COMMA params','params',3,'p_params','js_parser.py',72),
  ('params -> IDENTIFIER','params',1,'p_params_last','js_parser.py',76),
  ('compoundstmt -> LBRACE statements RBRACE','compoundstmt',3,'p_compoundstmt','js_parser.py',80),
  ('statements -> stmt SEMICOLON statements','statements',3,'p_statements','js_parser.py',84),
  ('statements -> <empty>','statements',0,'p_statements_empty','js_parser.py',88),
  ('stmt -> IF exp compoundstmt','stmt',3,'p_stmt_ifthen','js_parser.py',93),
  ('stmt -> IF exp compoundstmt ELSE compoundstmt','stmt',5,'p_stmt_ifthenelse','js_parser.py',98),
  ('stmt -> IDENTIFIER EQUAL exp','stmt',3,'p_stmt_assign','js_parser.py',103),
  ('stmt -> RETURN exp','stmt',2,'p_stmt_return','js_parser.py',108),
  ('stmt -> VAR IDENTIFIER EQUAL exp','stmt',4,'p_stmt_declare','js_parser.py',113),
  ('stmt -> VAR IDENTIFIER EQUAL FUNCTION LPAREN optparams RPAREN compoundstmt','stmt',8,'p_stmt_declare_funcexp','js_parser.py',117),
  ('stmt -> exp','stmt',1,'p_stmt_exp','js_parser.py',122),
  ('exp -> NOT exp','exp',2,'p_exp_not','js_parser.py',159),
  ('exp -> LPAREN exp RPAREN','exp',3,'p_exp_parens','js_parser.py',163),
  ('exp -> exp OROR exp','exp',3,'p_binop','js_parser.py',167),
  ('exp -> exp ANDAND exp','exp',3,'p_binop','js_parser.py',168),
  ('exp -> exp EQUALEQUAL exp','exp',3,'p_binop','js_parser.py',169),
  ('exp -> exp LT exp','exp',3,'p_binop','js_parser.py',170),
  ('exp -> exp GT exp','exp',3,'p_binop','js_parser.py',171),
  ('exp -> exp LE exp','exp',3,'p_binop','js_parser.py',172),
  ('exp -> exp GE exp','exp',3,'p_binop','js_parser.py',173),
  ('exp -> exp PLUS exp','exp',3,'p_binop','js_parser.py',174),
  ('exp -> exp MINUS exp','exp',3,'p_binop','js_parser.py',175),
  ('exp -> exp TIMES exp','exp',3,'p_binop','js_parser.py',176),
  ('exp -> exp DIVIDE exp','exp',3,'p_binop','js_parser.py',177),
  ('exp -> exp MODULO exp','exp',3,'p_binop','js_parser.py',178),
  ('exp -> IDENTIFIER LPAREN optargs RPAREN','exp',4,'p_exp_call','js_parser.py',182),
  ('optargs -> args','optargs',1,'p_optargs','js_parser.py',186),
  ('optargs -> <empty>','optargs',0,'p_optargs_empty','js_parser.py',190),
  ('args -> exp COMMA args','args',3,'p_args','js_parser.py',194),
  ('args -> exp','args',1,'p_args_last','js_parser.py',198),
  ('exp -> IDENTIFIER','exp',1,'p_exp_identifier','js_parser.py',202),
  ('exp -> NUMBER','exp',1,'p_exp_number','js_parser.py',206),
  ('exp -> STRING','exp',1,'p_exp_string','js_parser.py',210),
  ('exp -> TRUE','exp',1,'p_exp_true','js_parser.py',214),
  ('exp -> FALSE','exp',1,'p_exp_false','js_parser.py',218),
]
