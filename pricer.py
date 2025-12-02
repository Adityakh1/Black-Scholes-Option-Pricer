import math

# Function to calculate cumulative normal distribution
def norm_cdf(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))

# Black-Scholes price function
def black_scholes_price(S, K, T, r, sigma):
    if T <= 0 or sigma <= 0:
        call = max(0.0, S - K * math.exp(-r * T))
        put  = max(0.0, K * math.exp(-r * T) - S)
        return call, put
    d1 = (math.log(S / K) + (r + 0.5 * sigma * sigma) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    call = S * norm_cdf(d1) - K * math.exp(-r * T) * norm_cdf(d2)
    put = K * math.exp(-r * T) * norm_cdf(-d2) - S * norm_cdf(-d1)
    return call, put

print("\n--- Option Pricer (Black-Scholes Model) ---")

continue_program = True

while continue_program:

    # Input with error handling
    try:
        S = float(input("Enter Stock Price (S): "))
        K = float(input("Enter Strike Price (K): "))
        T = float(input("Enter Time to Maturity in years (T): "))
        r = float(input("Enter Risk-Free Rate (r) in decimal (example 0.05): "))
        sigma = float(input("Enter Volatility (σ) in decimal (example 0.20): "))
    except ValueError:
        print("Invalid input! Please enter numbers only.\n")
        continue  # Go back to start of loop

    # Calculate call and put prices
    call, put = black_scholes_price(S, K, T, r, sigma)

    # Print professional summary
    print("\n========== Option Pricing Summary ==========")
    print(f"Stock Price (S)       : {S:.2f}")
    print(f"Strike Price (K)      : {K:.2f}")
    print(f"Time to Maturity (T)  : {T} years")
    print(f"Risk-Free Rate (r)    : {r:.2%}")
    print(f"Volatility (σ)        : {sigma:.2%}")
    print("-------------------------------------------")
    print(f"Call Option Price      : {call:.4f}")
    print(f"Put Option Price       : {put:.4f}")
    print("===========================================\n")

    # Ask if user wants to calculate another option
    user_choice = input("Do you want to calculate another option? (yes/no): ").lower()
    if user_choice != "yes":
        continue_program = False
        print("Thank you for using the Option Pricer!")
