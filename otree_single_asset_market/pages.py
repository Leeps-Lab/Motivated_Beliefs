from otree_markets.pages import BaseMarketPage
from django.contrib.staticfiles.templatetags.staticfiles import static
from ._builtin import Page, WaitPage

class Market(BaseMarketPage):
    timeout_seconds = 10
    def before_next_page(self):
        if self.timeout_happened:
            self.player.save()

    #def is_displayed(self):
       # return self.round_number <= self.subsession.config.num_rounds

    def vars_for_template(self):
        ##load signal
        img_sig_url = static(
            'otree_single_asset_market/signal_{}.jpg'.format(self.player.signal_nature))
        ## load balls
        img_url = static(
            'otree_single_asset_market/balls2/balls_{}.jpg'.format(self.player.signal1_black))
        return {
            'signal1black': self.player.signal1_black,
            'signal1white': self.player.signal1_white,
            'img_url': img_url,
            'img_sig_url': img_sig_url,
        }

class Survey(Page):
    def vars_for_template(self):
            ##load signal
            def before_next_page(self):
                self.player.save()
            #def is_displayed(self):
              #  return self.round_number <= self.subsession.config.num_rounds

            img_sig_url = static(
                'otree_single_asset_market/signal_{}.jpg'.format(self.player.signal_nature))
            ## load balls
            img_url = static(
                'otree_single_asset_market/balls2/balls_{}.jpg'.format(self.player.signal1_black))
            return {
                'signal1black': self.player.signal1_black,
                'signal1white': self.player.signal1_white,
                'img_url': img_url,
                'img_sig_url': img_sig_url,
            }

    form_model = 'player'
    form_fields = ['Question_1', 'Question_2', 'Question_3']

class Wait(WaitPage):
    pass


page_sequence = [Market, Survey, Wait]