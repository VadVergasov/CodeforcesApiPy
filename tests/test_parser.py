"""
Testing parse methods
"""

from codeforces_api import CodeforcesParser


def test_get_solution():
    cf_parser = CodeforcesParser()
    solution = cf_parser.get_solution(contest_id=4, submit_id=21563028)
    assert (
        solution
        == '#include <iostream>\n\nusing namespace std;\n\nint main()\n{\n    int w;\n    cin>>w;\n    if(w%2==0&&w!=0&&w>0&&w!=2){\n        cout<<"YES";\n    }else{\n        cout<<"NO";\n    }\n    return 0;\n}\n'
    )


def test_get_tags():
    cf_parser = CodeforcesParser()
    tags = cf_parser.get_tags(contest_id=4, index="A")
    assert tags == ["brute force", "math"]
    tags = cf_parser.get_tags(contest_id=4, index="A", include_rating=True)
    assert tags == ["*800", "brute force", "math"]
