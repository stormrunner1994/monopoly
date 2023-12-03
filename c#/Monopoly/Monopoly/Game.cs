using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Monopoly
{        
    public class Game
    {
        private Board Board;
        private Card[] EventCards;
        private Card[] CommunityCards;
        private List<Street> AvailableStreets;
        private List<Player> Players;
        private int Zahl;

        public Game() {
            Init();        
        }

        private void Init()
        {
            EventCards = new Card[16];
            CommunityCards = new Card[16];
            Math.Round(0.2);
        }


        public void ComputeNextRound()
        {

        }

        public void StartNewGame()
        {
        }

        public bool IsGameFinished()
        {
            return false;
        }
    }
}
