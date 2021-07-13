
#include  <iostream>
#include <vector>
#include <string>
#include <stack>
using namespace std;

//判断是否为操作符
bool isOperator(char op)
{
	return (op == '+' || op == '-' || op == '*' || op == '/');
}

//判断是否为数字
bool isDigit(char op)
{
	return  (op >= '0' && op <= '9');
}

//计算表达式结果
int cal(int left, int right, char op)
{
	int res = 0;
	if (op == '+')
		res = left + right;
	else if (op == '-')
		res = left - right;
	else if (op == '*')
		res = left * right;
	else if (op == '/')
		res = left / right;
	return res;
}

//判断运算符优先级
int pirority(char op)
{
	if (op == '+' || op == '-')
		return 1;
	if (op == '*' || op == '/')
		return 2;
	else
		return 0;
}

//逆波兰表达式转中缀表达式
int evalRPN(string &tokens)
{
	if (tokens.size() <= 0)
		return 0;
	stack<int> s1;//创建辅助栈
	int left = 0, right = 0;//定义左/右操作数
	int result = 0;//定义中间结果
	string temp;
	for (unsigned int i = 0; i < tokens.size(); i++ )
	{
		
		if (isDigit(tokens[i]))//扫描数字入栈
		{
			temp.push_back(tokens[i]);
		}
		else if (tokens[i] == ' ')
		{
			if (temp.size() > 0)   //防止运算符后面跟分隔符，所以判断一下temp里面是否有数字
			{
				s1.push(atoi(temp.c_str()));
				temp.clear();
			}
		}
		else if (isOperator(tokens[i]) && !s1.empty())
		{
			//防止数字后面直接跟运算符，所以这里也要判断一下temp是否还有数字没有提取出来
			if (temp.size() > 0)
			{
				s1.push(atoi(temp.c_str()));
				temp.clear();
			}
			right = s1.top();
			s1.pop();
			
			left = s1.top();
			s1.pop();
		
			result = cal(left, right, tokens[i]);
			s1.push(result);
		}
		
	}
	if (!s1.empty())
	{
		result = s1.top();
		s1.pop();
	}

	return result;
}




//中缀表达式转逆波兰表达式
vector<char> infixToPRN(const string & token)
{
	vector<char> v1;
	int len = token.size();//string的长度
	if (len == 0)
		return v1;

	stack<char> s1;//存放逆波兰式的结果
	int outLen = 0;
	for (int i = 0; i < len ; i++)
	{
		if (token[i] == ' ')//跳过空格
			continue;
		if (isDigit(token[i]) )//若是数字，直接输出
		{
			v1.push_back(token[i]);
		}
		else if (token[i] == '(')//如果是'('，则压栈
		{
			s1.push(token[i]);
		}else if (token[i] == ')')//如果是')'， 则栈中运算符逐个出栈并输出，直至遇到'('。 '('出栈并丢弃
		{
			while (s1.top() != '(')
			{
				v1.push_back( s1.top());
				s1.pop();
			}
			s1.pop();//此时栈中为')'，跳过
		}
		while (isOperator(token[i]))//如果是运算符
		{
			//空栈||或者栈顶为)||新来的元素优先级更高  
			if( s1.empty() || s1.top() == '(' || pirority(token[i]) > pirority(s1.top()))
			{
				s1.push(token[i]);// 当前操作符优先级比栈顶高， 将栈顶操作符写入后缀表达式
				break;
			}else 
			{
				v1.push_back(s1.top());
				s1.pop();
			}
			 
			
		}
	}
	while (!s1.empty())//输入结束，将栈中剩余操作符出栈输出
	{
		v1.push_back(s1.top());
		s1.pop();
	}
	return v1;
}
int main()
{
	//vector<string> sRPN = {"4", "13", "5" , "/", "+"};//逆波兰表达式
	//cout << "逆波兰表达式结果为：" << evalRPN(sRPN) <<endl;

	//vector<string> fix = {"4", "+", "13", "/", "5"};//中缀表达式
	string fix = "2+2*(1*2-4/2)*1";
	vector<char> RPN = infixToPRN(fix);
	string s_fix;
	for (auto it = RPN.begin(); it != RPN.end(); it++)
	{
		cout << *it << " ";
		s_fix += *it;
		s_fix += " ";
	}
	cout << endl;
	cout << "逆波兰表达式结果为：" << evalRPN(s_fix) << endl;


	
	system("pause");

	return 0;
	
}

