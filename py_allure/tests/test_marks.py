import sys,pytest
# 标记与分组
class TestMarks(object):
    @pytest.mark.skip(reason="not implementation")
    def test_the_unknown(self):
        """
        跳过不执行
        :return:
        """
        assert 0
    @pytest.mark.skipif(sys.version_info<(3,7),reason="requires python3.7 or higher")
    def test_skipif(self):
        """版本小于3.7不执行"""
        assert 1
    @pytest.mark.xfail
    def test_xfail(self):
        """
        Indicate that you expect it to fail
        这条用例失败时，测试结果被标记为xfail（expected to fail），并且不打印错误信息。
        这条用例执行成功时，测试结果被标记为xpassed（unexpectedly passing）
        """
        assert 0
    @pytest.mark.xfail(run=False)
    def test_xfail_not_run(self):
        """run=false 表示不执行这条用例"""
        assert 0