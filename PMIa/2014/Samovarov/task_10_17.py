#������ 10. ������� 11.
#1-50. �������� ��������� "��������� ����������" ��� ����. ������������ ������ ���� ������������� 30 �������, ������� ����� ������������ ����� �������� ����������������: ����, ��������, �������� � ��������. ���� ������� ���, ����� ������������ ��� �� ������ ����� ��� ������ �� ������ "����", �� � ���������� �� ���� �� �������������, ������� �� ����� ��������� ������ ��������.

#Samovarov K.
#28.05.2016
import random

class solution:
    def main(self):
        self.max_stat=30
        print('''
             ***��������� ����������***
       � ���  ���� 30 ����������, ������� �� ������
������������ �����: �����, ���������, ���������� � ���������.
              ������� ������!
    (��� ���� ��� �� ��������� ������ ������� "�����")
''')
        self.sila=0
        self.zdorov=0
        self.um=0
        self.lovkost=0      
        while True:
            self.printhar()
            print("�������� ����� �������������: ", self.max_stat)
            if (self.max_stat<0):
                print("�������������� ����")
            vvod=input("\n������� �������������� ������� ������ ��������: ")
            if vvod=="����":
                self.strenghth(self.max_stat,self.sila)
                continue
            if vvod=="��������":
                self.health(self.max_stat,self.zdorov)
                continue
            if vvod=="���������":
                self.mind(self.max_stat,self.um)
                continue
            if vvod=="��������":
                self.agility(self.max_stat,self.um)
                continue
            if vvod=="�����":
                print("\n\n\n!!!��������!!!")
                self.printhar()
                input("\n\n\n������� Enter ��� �������� ����")
                return

        
    def strenghth(self,max_stat,sila):
        while True:
            print("\n����� ��������� � ������ �������������� ������� \"�����\"\n����� ���� ", self.sila)
            whattodo=input("��� ������ �������(��������/������):")
            if(whattodo=="�����"):
                return
            if(whattodo=="��������"):
                dobav=int(input("������� ����� ���� ������ ��������? "))
                if self.max_stat<dobav:
                    print("�� ������� ����� �������������.")
                    continue
                self.sila+=dobav
                self.max_stat-=dobav
                print("�������� ����� �������������: ", self.max_stat)
                continue
            elif(whattodo=="������"):
                if self.sila==0:
                    print("���������� �������� �.�.  ���� ����� 0")
                    continue
                otnat=int(input("������� ����� ���� ������ ������? "))
                if self.max_stat<otnat:
                    print("�� ������� ����� �������������.")
                    continue
                if (otnat>self.sila):
                    print("���������� ������� ������.")
                    continue
                self.sila-=otnat
                self.max_stat+=otnat
                print("�������� ����� �������������: ", self.max_stat)
                continue

    def health(self,max_stat,zdorov):
        while True:
            print("\n����� ��������� � ������ �������������� ������� \"�����\"\n����� �������� ", self.zdorov)
            whattodo=input("��� ������ �������(��������/������):")
            if(whattodo=="�����"):
                return
            if(whattodo=="��������"):
                dobav=int(input("������� ����� �������� ������ ��������? "))
                if self.max_stat<dobav:
                    print("�� ������� ����� �������������.")
                    continue
                self.zdorov+=dobav
                self.max_stat-=dobav
                print("�������� ����� �������������: ", self.max_stat)
                continue
            elif(whattodo=="������"):
                if self.zdorov==0:
                    print("���������� �������� �.�. �������� ����� 0")
                    continue
                otnat=int(input("������� ����� �������� ������ ������? "))
                if (otnat>self.zdorov):
                    print("���������� ������� ������.")
                    continue
                self.zdorov-=otnat
                self.max_stat+=otnat
                print("�������� ����� �������������: ", self.max_stat)
                continue

    def mind(self,max_stat,mind):
            while True:
                print("\n����� ��������� � ������ �������������� ������� \"�����\"\n����� ���������� ", self.um)
                whattodo=input("��� ������ �������(��������/������):")
                if(whattodo=="�����"):
                    return
                if(whattodo=="��������"):
                    dobav=int(input("������� ����� ���������� ������ ��������? "))
                    if self.max_stat<dobav:
                        print("�� ������� ����� �������������.")
                        continue
                    self.um+=dobav
                    self.max_stat-=dobav
                    print("�������� ����� �������������: ", self.max_stat)
                    continue
                elif(whattodo=="������"):
                    if self.um==0:
                        print("���������� �������� �.�. ��������� ����� 0")
                        continue
                    otnat=int(input("������� ����� ���������� ������ ������? "))
                    if self.max_stat<otnat:
                        print("�� ������� ����� �������������.")
                        continue
                    if (otnat>self.um):
                        print("���������� ������� ������.")
                        continue
                    self.um-=otnat
                    self.max_stat+=otnat
                    print("�������� ����� �������������: ", self.max_stat)
                    continue
    
    def agility(self,max_stat,lovkost):
            while True:
                print("\n����� ��������� � ������ �������������� ������� \"�����\"\n����� �������� ", self.lovkost)
                whattodo=input("��� ������ �������(��������/������):")
                if(whattodo=="�����"):
                    return
                if(whattodo=="��������"):
                    dobav=int(input("������� ����� �������� ������ ��������? "))
                    if self.max_stat<dobav:
                        print("�� ������� ����� �������������.")
                        continue
                    self.lovkost+=dobav
                    self.max_stat-=dobav
                    print("�������� ����� �������������: ", self.max_stat)
                    continue
                elif(whattodo=="������"):
                    if self.lovkost==0:
                        print("���������� �������� �.�. �������� ����� 0")
                        continue
                    otnat=int(input("������� ����� �������� ������ ������? "))
                    if self.max_stat<otnat:
                        print("�� ������� ����� �������������.")
                        continue
                    if (otnat>self.lovkost):
                        print("���������� ������� ������.")
                        continue
                    self.lovkost-=otnat
                    self.max_stat+=otnat
                    print("�������� ����� �������������: ", self.max_stat)
                    continue




            

    def printhar(self):
        print("\n�������������� ���������:\n���� = ",self.sila,"\n��������� = ",self.um,"\n�������� = ", self.zdorov,"\n�������� = ",self.lovkost)
        return

obj = solution()
obj.main()


#strength, healh, mind, agility