import React, { useState, useEffect } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { useToast } from '@/hooks/use-toast';
import { 
  DollarSign, 
  Euro, 
  Banknote,
  TrendingUp,
  TrendingDown,
  Leaf,
  Shield,
  AlertTriangle,
  X,
  ChevronDown,
  ChevronUp,
  Bot,
  Sun,
  Moon,
  User,
  Bell,
  ArrowUpRight,
  ArrowDownLeft,
  Filter,
  Search,
  Download,
  CheckCircle,
  AlertCircle,
  XCircle,
  Sparkles,
  Activity
} from 'lucide-react';

// Types
interface Balance {
  USD: number;
  EUR: number;
  AUD: number;
}

interface Transaction {
  tx_id: string;
  timestamp: string;
  pair: string;
  rate: number;
  amount_src: number;
  amount_dst: number;
  balances_before: Balance;
  balances_after: Balance;
  carbon: {
    kg: number;
    badge: string;
  };
  compliance: string;
}

// Mock data (fallback)
const mockBalances: Balance = {
  USD: 5000.0,
  EUR: 1000,
  AUD: 23500.0
};

const WalletDashboard = () => {
  const [isDarkMode, setIsDarkMode] = useState(() => {
    if (typeof window !== 'undefined') {
      const saved = localStorage.getItem('theme');
      if (saved) return saved === 'dark';
      return window.matchMedia('(prefers-color-scheme: dark)').matches;
    }
    return false;
  });
  
  const [balances, setBalances] = useState<Balance>(mockBalances);
  const [transactions, setTransactions] = useState<Transaction[]>([]);
  const [expandedCard, setExpandedCard] = useState<string | null>(null);
  const [expandedTransaction, setExpandedTransaction] = useState<string | null>(null);
  const [complianceExpanded, setComplianceExpanded] = useState(false);
  const [filterStatus, setFilterStatus] = useState<string>('All');
  const [searchQuery, setSearchQuery] = useState('');
  
  const { toast } = useToast();

  // Theme toggle
  useEffect(() => {
    const root = document.documentElement;
    if (isDarkMode) {
      root.classList.add('dark');
    } else {
      root.classList.remove('dark');
    }
    localStorage.setItem('theme', isDarkMode ? 'dark' : 'light');
  }, [isDarkMode]);

  // Load data
  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      // Load balances
      const balanceResponse = await fetch('/fx_data/balances.json');
      if (balanceResponse.ok) {
        const balanceData = await balanceResponse.json();
        setBalances(balanceData);
      }

      // Load transactions
      const txResponse = await fetch('/fx_data/transactions_log.json');
      if (txResponse.ok) {
        const txData = await txResponse.json();
        setTransactions(txData);
        
        // Show toast for flagged transactions
        const flaggedTx = txData.filter((tx: Transaction) => tx.compliance !== 'Clear');
        flaggedTx.forEach((tx: Transaction) => {
          if (tx.compliance === 'Review') {
            toast({
              title: "Transaction flagged for review",
              description: "High velocity or threshold exceeded",
              variant: "default",
              className: "bg-warning text-warning-foreground border-warning/20",
            });
          } else if (tx.compliance === 'Blocked') {
            toast({
              title: "Transaction blocked",
              description: "Policy rules violation",
              variant: "destructive",
            });
          }
        });
      }
    } catch (error) {
      console.error('Error loading data:', error);
    }
  };

  // Calculate KPIs
  const totalBalanceAUD = Object.entries(balances).reduce((total, [currency, amount]) => {
    // Simple conversion rates for demo
    const rates = { USD: 1.5, EUR: 1.6, AUD: 1 };
    return total + (amount * (rates[currency as keyof typeof rates] || 1));
  }, 0);

  const recentTransactions = transactions.slice(-7);
  const monthlyCarbon = transactions
    .filter(tx => new Date(tx.timestamp).getMonth() === new Date().getMonth())
    .reduce((sum, tx) => sum + tx.carbon.kg, 0);

  // Currency icons
  const getCurrencyIcon = (currency: string) => {
    switch (currency) {
      case 'USD': return <DollarSign className="h-6 w-6" />;
      case 'EUR': return <Euro className="h-6 w-6" />;
      case 'AUD': return <Banknote className="h-6 w-6" />;
      default: return <DollarSign className="h-6 w-6" />;
    }
  };

  // Status icons
  const getStatusIcon = (status: string) => {
    switch (status) {
      case 'Clear': return <CheckCircle className="h-4 w-4 text-success" />;
      case 'Review': return <AlertCircle className="h-4 w-4 text-warning" />;
      case 'Blocked': return <XCircle className="h-4 w-4 text-destructive" />;
      default: return <CheckCircle className="h-4 w-4 text-success" />;
    }
  };

  // Filter transactions
  const filteredTransactions = transactions.filter(tx => {
    const matchesFilter = filterStatus === 'All' || tx.compliance === filterStatus;
    const matchesSearch = tx.pair.toLowerCase().includes(searchQuery.toLowerCase());
    return matchesFilter && matchesSearch;
  });

  // Get currency transactions for balance card
  const getCurrencyTransactions = (currency: string) => {
    return transactions
      .filter(tx => tx.pair.includes(currency))
      .slice(-3);
  };

  return (
    <div className="min-h-screen bg-background theme-transition">
      {/* Header */}
      <header className="sticky top-0 z-50 border-b bg-card/80 backdrop-blur-sm">
        <div className="container mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-4">
              <div className="flex items-center space-x-2">
                <div className="h-8 w-8 rounded-lg bg-gradient-to-br from-primary to-secondary flex items-center justify-center">
                  <Sparkles className="h-5 w-5 text-white" />
                </div>
                <h1 className="text-xl font-bold">Aiva</h1>
              </div>
              <div className="hidden md:flex items-center space-x-2 text-sm text-muted-foreground">
                <div className="h-2 w-2 rounded-full bg-success animate-pulse"></div>
                <span>API connected</span>
              </div>
            </div>
            
            <div className="flex items-center space-x-4">
              <Button
                variant="ghost"
                size="icon"
                onClick={() => setIsDarkMode(!isDarkMode)}
                className="theme-transition"
              >
                {isDarkMode ? <Sun className="h-4 w-4" /> : <Moon className="h-4 w-4" />}
              </Button>
              <Button variant="ghost" size="icon">
                <Bell className="h-4 w-4" />
              </Button>
              <Button variant="ghost" size="icon">
                <User className="h-4 w-4" />
              </Button>
            </div>
          </div>
        </div>
      </header>

      <div className="container mx-auto px-6 py-8 space-y-8">
        {/* Hero Section */}
        <div className="text-center space-y-4">
          <div className="space-y-2">
            <h2 className="text-4xl font-bold bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent">
              Welcome to Aiva
            </h2>
            <p className="text-xl text-muted-foreground">
              Manage your multi-currency wallet with intelligence
            </p>
          </div>
          
          {/* KPI Strip */}
          <div className="flex flex-wrap justify-center gap-8 mt-8">
            <div className="text-center">
              <div className="text-3xl font-bold text-primary">
                ${totalBalanceAUD.toLocaleString()}
              </div>
              <div className="text-sm text-muted-foreground">Total Balance (AUD)</div>
            </div>
            <div className="text-center">
              <div className="text-3xl font-bold text-secondary">
                {recentTransactions.length}
              </div>
              <div className="text-sm text-muted-foreground">7d Transactions</div>
            </div>
            <div className="text-center">
              <div className="text-3xl font-bold text-success">
                {monthlyCarbon.toFixed(2)} kg
              </div>
              <div className="text-sm text-muted-foreground">CO₂ This Month</div>
            </div>
          </div>
        </div>

        {/* Balance Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {Object.entries(balances).map(([currency, amount]) => (
            <Card 
              key={currency}
              className="card-hover cursor-pointer rounded-2xl"
              onClick={() => setExpandedCard(expandedCard === currency ? null : currency)}
            >
              <CardContent className="p-6">
                <div className="flex items-start justify-between">
                  <div className="space-y-2">
                    <div className="flex items-center space-x-2">
                      {getCurrencyIcon(currency)}
                      <span className="font-semibold text-lg">{currency}</span>
                    </div>
                    <div className="text-3xl font-bold">
                      {currency === 'USD' && '$'}
                      {currency === 'EUR' && '€'}
                      {currency === 'AUD' && 'A$'}
                      {amount.toLocaleString()}
                    </div>
                    <Badge variant="outline" className="bg-success/10 text-success border-success/20">
                      <Leaf className="h-3 w-3 mr-1" />
                      Low Carbon
                    </Badge>
                  </div>
                  <ChevronDown className={`h-5 w-5 transition-transform ${expandedCard === currency ? 'rotate-180' : ''}`} />
                </div>
                
                {expandedCard === currency && (
                  <div className="mt-6 pt-6 border-t space-y-4 animate-fade-in">
                    <div className="space-y-2">
                      <h4 className="font-semibold text-sm">Last 3 Transactions</h4>
                      {getCurrencyTransactions(currency).map(tx => (
                        <div key={tx.tx_id} className="flex justify-between items-center text-sm">
                          <span className="text-muted-foreground">{tx.pair}</span>
                          <div className="flex items-center space-x-2">
                            <span className="font-medium">
                              {tx.pair.startsWith(currency) ? '-' : '+'}
                              {(tx.pair.startsWith(currency) ? tx.amount_src : tx.amount_dst).toLocaleString()}
                            </span>
                            {getStatusIcon(tx.compliance)}
                          </div>
                        </div>
                      ))}
                    </div>
                    <div className="flex space-x-2">
                      <Button size="sm" className="flex-1">Convert</Button>
                      <Button size="sm" variant="outline" className="flex-1">View All</Button>
                    </div>
                  </div>
                )}
              </CardContent>
            </Card>
          ))}
        </div>

        {/* Smart FX Recommendation */}
        <Card className="rounded-2xl border-primary/20 bg-gradient-to-br from-primary/5 to-secondary/5">
          <CardHeader>
            <div className="flex items-center justify-between">
              <div className="flex items-center space-x-3">
                <div className="h-10 w-10 rounded-full bg-primary/10 flex items-center justify-center">
                  <Bot className="h-5 w-5 text-primary" />
                </div>
                <div>
                  <CardTitle className="flex items-center space-x-2">
                    <span>Smart FX Recommendation</span>
                    <Badge variant="secondary" className="text-xs">Today</Badge>
                  </CardTitle>
                </div>
              </div>
            </div>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="bg-card/50 rounded-xl p-4 border">
              <p className="text-sm text-muted-foreground mb-2">AI Insight</p>
              <p className="font-medium">
                AUD is currently strong vs USD (+2.1%). Optimal time to convert based on 7-day trend analysis.
              </p>
            </div>
            
            {/* Mini Sparkline */}
            <div className="flex items-center space-x-4">
              <div className="flex-1">
                <div className="h-12 bg-gradient-to-r from-primary/20 to-secondary/20 rounded-lg flex items-end space-x-1 p-2">
                  {[0.65, 0.67, 0.66, 0.68, 0.69, 0.67, 0.71].map((value, i) => (
                    <div
                      key={i}
                      className="bg-primary flex-1 rounded-sm opacity-70"
                      style={{ height: `${value * 100}%` }}
                    />
                  ))}
                </div>
                <div className="text-xs text-muted-foreground mt-1">AUD/USD 7d trend</div>
              </div>
              <div className="space-y-2">
                <Button className="w-full">Convert Now</Button>
                <Button variant="outline" size="sm" className="w-full text-xs">
                  Why? 
                  <Activity className="h-3 w-3 ml-1" />
                </Button>
              </div>
            </div>
          </CardContent>
        </Card>

        {/* Transaction Timeline */}
        <Card className="rounded-2xl">
          <CardHeader>
            <div className="flex items-center justify-between">
              <CardTitle className="flex items-center space-x-2">
                <Activity className="h-5 w-5" />
                <span>Transaction Timeline</span>
              </CardTitle>
              <div className="flex items-center space-x-2">
                <div className="flex items-center space-x-1">
                  {['All', 'Clear', 'Review', 'Blocked'].map(status => (
                    <Button
                      key={status}
                      variant={filterStatus === status ? 'default' : 'ghost'}
                      size="sm"
                      onClick={() => setFilterStatus(status)}
                      className="text-xs"
                    >
                      {status}
                    </Button>
                  ))}
                </div>
                <div className="flex items-center space-x-2">
                  <Search className="h-4 w-4 text-muted-foreground" />
                  <input
                    type="text"
                    placeholder="Search pairs..."
                    className="px-2 py-1 text-sm border rounded bg-background"
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                  />
                </div>
              </div>
            </div>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="space-y-2">
              {filteredTransactions.map((tx, index) => (
                <div
                  key={tx.tx_id}
                  className="timeline-item rounded-xl p-4 border cursor-pointer"
                  onClick={() => setExpandedTransaction(expandedTransaction === tx.tx_id ? null : tx.tx_id)}
                >
                  <div className="flex items-center justify-between">
                    <div className="flex items-center space-x-4">
                      {getStatusIcon(tx.compliance)}
                      <div>
                        <div className="font-medium">{tx.pair.replace('_', ' → ')}</div>
                        <div className="text-sm text-muted-foreground">
                          {new Date(tx.timestamp).toLocaleString()}
                        </div>
                      </div>
                      <div className="text-right">
                        <div className="font-medium">
                          {tx.amount_src} → {tx.amount_dst}
                        </div>
                        <div className="text-sm text-muted-foreground">
                          Rate: {tx.rate}
                        </div>
                      </div>
                    </div>
                    <div className="flex items-center space-x-2">
                      <Badge 
                        variant="outline" 
                        className={`${
                          tx.carbon.badge === 'Low' ? 'bg-success/10 text-success border-success/20' :
                          tx.carbon.badge === 'Medium' ? 'bg-warning/10 text-warning border-warning/20' :
                          'bg-destructive/10 text-destructive border-destructive/20'
                        }`}
                      >
                        {tx.carbon.kg} kg CO₂ · {tx.carbon.badge}
                      </Badge>
                      <ChevronDown className={`h-4 w-4 transition-transform ${expandedTransaction === tx.tx_id ? 'rotate-180' : ''}`} />
                    </div>
                  </div>
                  
                  {expandedTransaction === tx.tx_id && (
                    <div className="mt-4 pt-4 border-t space-y-3 animate-fade-in">
                      <div className="grid grid-cols-2 gap-4 text-sm">
                        <div>
                          <span className="text-muted-foreground">Before:</span>
                          <div className="font-mono text-xs">
                            USD: {tx.balances_before.USD}, EUR: {tx.balances_before.EUR}, AUD: {tx.balances_before.AUD}
                          </div>
                        </div>
                        <div>
                          <span className="text-muted-foreground">After:</span>
                          <div className="font-mono text-xs">
                            USD: {tx.balances_after.USD}, EUR: {tx.balances_after.EUR}, AUD: {tx.balances_after.AUD}
                          </div>
                        </div>
                      </div>
                      {tx.compliance !== 'Clear' && (
                        <div className="bg-muted/50 rounded-lg p-3">
                          <div className="text-sm font-medium mb-1">Compliance Status: {tx.compliance}</div>
                          <div className="text-xs text-muted-foreground">
                            This transaction was flagged for manual review due to policy thresholds.
                          </div>
                        </div>
                      )}
                    </div>
                  )}
                </div>
              ))}
            </div>
          </CardContent>
        </Card>

        {/* Collapsible Compliance & Carbon Panel */}
        <Card className="rounded-2xl">
          <CardHeader>
            <div 
              className="flex items-center justify-between cursor-pointer"
              onClick={() => setComplianceExpanded(!complianceExpanded)}
            >
              <CardTitle className="flex items-center space-x-2">
                <Shield className="h-5 w-5" />
                <span>Compliance & Carbon Information</span>
              </CardTitle>
              <ChevronDown className={`h-5 w-5 transition-transform ${complianceExpanded ? 'rotate-180' : ''}`} />
            </div>
          </CardHeader>
          {complianceExpanded && (
            <CardContent className="space-y-6 animate-fade-in">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div className="space-y-4">
                  <h4 className="font-semibold">Compliance Legend</h4>
                  <div className="space-y-3">
                    <div className="flex items-center space-x-3">
                      <CheckCircle className="h-4 w-4 text-success" />
                      <span className="text-sm">Clear - Transaction approved</span>
                    </div>
                    <div className="flex items-center space-x-3">
                      <AlertCircle className="h-4 w-4 text-warning" />
                      <span className="text-sm">Review - Manual review required</span>
                    </div>
                    <div className="flex items-center space-x-3">
                      <XCircle className="h-4 w-4 text-destructive" />
                      <span className="text-sm">Blocked - Policy violation</span>
                    </div>
                  </div>
                </div>
                
                <div className="space-y-4">
                  <h4 className="font-semibold">Carbon Impact Legend</h4>
                  <div className="space-y-3">
                    <div className="flex items-center justify-between">
                      <span className="text-sm">Low Impact</span>
                      <Badge variant="outline" className="bg-success/10 text-success border-success/20">
                        &lt; 0.5 kg CO₂
                      </Badge>
                    </div>
                    <div className="flex items-center justify-between">
                      <span className="text-sm">Medium Impact</span>
                      <Badge variant="outline" className="bg-warning/10 text-warning border-warning/20">
                        0.5 - 2.0 kg CO₂
                      </Badge>
                    </div>
                    <div className="flex items-center justify-between">
                      <span className="text-sm">High Impact</span>
                      <Badge variant="outline" className="bg-destructive/10 text-destructive border-destructive/20">
                        &gt; 2.0 kg CO₂
                      </Badge>
                    </div>
                  </div>
                </div>
              </div>
              
              <div className="pt-4 border-t">
                <Button variant="outline" className="w-full md:w-auto">
                  <Download className="h-4 w-4 mr-2" />
                  Export Summary
                </Button>
              </div>
            </CardContent>
          )}
        </Card>
      </div>
      
      {/* Footer */}
      <footer className="border-t bg-card/50 py-8">
        <div className="container mx-auto px-6 text-center text-sm text-muted-foreground">
          © 2025 Aiva. All rights reserved.
        </div>
      </footer>
    </div>
  );
};

export default WalletDashboard;